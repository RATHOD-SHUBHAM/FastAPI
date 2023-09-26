from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import lang_predict
from app.model.model import __version__ as model_version


app = FastAPI()

class InputText(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    language: str

@app.get("/")
async def root():
    return {"message": "Welcome To Language Detection APP", "health_check": "OK", "model_version": model_version}


@app.post("/lang_prediction", response_model=PredictionOutput, status_code=201)
def predict(payload: InputText):
    language = lang_predict(payload.text)
    return {"language": language}


