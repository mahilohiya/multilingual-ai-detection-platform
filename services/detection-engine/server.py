from fastapi import FastAPI
from pydantic import BaseModel

from multilingual_ai_detector import MultilingualAIDetector


app = FastAPI(
    title="Detection Engine Service",
    description="Multilingual & Paraphrase-Resistant AI Text Detection Microservice",
    version="2.0.0",
)

detector = MultilingualAIDetector()


class AnalyzeRequest(BaseModel):
    text: str
    language: str = "auto"


class CrossLingualRequest(BaseModel):
    text: str


@app.get("/")
def health():
    return {
        "status": "Detection Engine Running",
        "model_version": detector.get_model_info()["model_version"],
    }


@app.post("/analyze")
def analyze_text(request: AnalyzeRequest):
    result = detector.analyze(request.text, request.language)
    return result


@app.post("/analyze_crosslingual")
def analyze_crosslingual(request: CrossLingualRequest):
    return detector.analyze_crosslingual(request.text)


@app.get("/models")
def model_info():
    return detector.get_model_info()

