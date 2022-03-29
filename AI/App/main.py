from time import time
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import pickle
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
from store_data import predictionOverview

app = FastAPI()
model = pickle.load(open('App/model/Log_reg.sav', 'rb'))

graphs = {}
graphs['c'] = Counter('python_request_operations_total')


class Data(BaseModel):
    CustomerId: int
    Surname: str
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


@app.get("/")
def read_root():
    return {"Hello": "churn"}


@app.post("/prediction")
def prediction(data: Data):
    req = data.json()
    data = pd.read_json(req, orient='index').transpose()
    pred = model.predict(data)
    predictionOverview(data)
    "Not Churn" if pred == [0] else "CHURN"
    return {"pred": "Not Churn" if pred == [0] else "CHURN"}


if __name__ == "__main__":
    uvicorn.run()
