from fastapi import FastAPI
from pydantic import BaseModel

# Non Docker
# from model.model import Prediction
# from model.model import __version__ as model_version

# Docker
from app.model.model import Prediction
from app.model.model import __version__ as model_version

app = FastAPI()


# Data Validation
class model_input(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


class PredictionOutput(BaseModel):
    prediction: str

@app.get("/")
async def root():
    return {"message": "Welcome To Language Detection APP", "health_check": "OK", "model_version": model_version}


@app.post("/diabetes_prediction",response_model=PredictionOutput, status_code=201)
def predict(payload: model_input):
    preg = payload.pregnancies
    glu = payload.Glucose
    bp = payload.BloodPressure
    skin = payload.SkinThickness
    insulin = payload.Insulin
    bmi = payload.BMI
    dpf = payload.DiabetesPedigreeFunction
    age = payload.Age

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = Prediction.diabetesPrediction(input_list)

    return {'prediction' : prediction}