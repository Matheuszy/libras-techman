from fastapi import FastAPI
from pydantic import BaseModel

from core.classificador_hibrido import ClassificadorHibrido
from core.detector_emocao import DetectorEmocao


app = FastAPI(title="Libras-TechMan API")

class RequestMock(BaseModel):
    pass

classificador = ClassificadorHibrido()
emocao_engine = DetectorEmocao()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test")
def test():

    return {
        "message": "API Libras-TechMan rodando"
    }

@app.get("/predict")
def predict():

    return {
        "letra": "A",
        "confianca": 0.99,
        "metodo": "DEMO"
    }