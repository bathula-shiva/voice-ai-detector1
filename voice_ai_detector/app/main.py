from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from voice_ai_detector.app.audio_utils import extract_features
from voice_ai_detector.app.model import predict

app = FastAPI(title="Voice AI Detector")

# ✅ Correct paths (important)
app.mount("/static", StaticFiles(directory="voice_ai_detector/static"), name="static")
templates = Jinja2Templates(directory="voice_ai_detector/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/detect")
async def detect_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    features = extract_features(audio_bytes)
    prediction = predict(features)

    return {
        "prediction": prediction["result"],
        "confidence": prediction["confidence"]
    }
