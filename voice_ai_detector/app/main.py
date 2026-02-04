from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.requests import Request

from app.audio_utils import extract_features
from app.model import predict

app = FastAPI(title="Voice AI Detector")

# STATIC & TEMPLATES (outside app)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/detect")
async def detect_voice(audio_url: str):
    features = extract_features(audio_url)
    result = predict(features)

    return JSONResponse({
        "prediction": result
    })
