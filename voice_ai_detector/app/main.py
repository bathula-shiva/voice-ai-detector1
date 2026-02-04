from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

from app.audio_utils import extract_features
from app.model import predict

app = FastAPI(
    title="Voice AI Detector",
    version="0.1.0"
)

# ---------- Static & Templates ----------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------- Home UI ----------
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# ---------- Detection API ----------
@app.post("/detect")
async def detect_voice(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{file.filename}"

    # Save uploaded audio
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Feature extraction + prediction
    features = extract_features(file_path)
    prediction, confidence = predict(features)

    # Cleanup
    os.remove(file_path)

    return {
        "prediction": prediction,
        "confidence": confidence
    }
