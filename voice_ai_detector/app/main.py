from fastapi import FastAPI, UploadFile, File
from app.audio_utils import extract_features
from app.model import predict

app = FastAPI(title="Voice AI Detector")

@app.post("/detect")
async def detect_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    features = extract_features(audio_bytes)
    prediction = predict(features)

    return {
        "prediction": prediction["result"],
        "confidence": prediction["confidence"]
    }
