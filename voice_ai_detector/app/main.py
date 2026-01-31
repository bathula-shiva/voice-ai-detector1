from fastapi import FastAPI, UploadFile, File
from app.audio_utils import extract_features
from app.model import predict_voice

app = FastAPI(title="Voice AI Detector")

@app.post("/detect")
async def detect_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    features = extract_features(audio_bytes)
    prediction = predict_voice(features)

    return {
        "prediction": prediction["result"],
        "confidence": prediction["confidence"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
