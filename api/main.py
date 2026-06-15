## backend code

from fastapi import FastAPI
from app.schemas import WeatherInput
from app.predictor import predict_weather


app = FastAPI(title="Thunderstrom Prediction API")

# to ensure app is running
@app.get("/")
def home():
    return {"message": "Weather Prediction API is running"}

# microservice given the list of features we will be going to get the prediction of the weather
@app.post("/predict")
def predict(data: WeatherInput):
    features = data.to_list()
    result = predict_weather(features) # prob , pred
    return result


## uvicorn api.main:app --host 0.0.0.0 --port 8000  command to run the app