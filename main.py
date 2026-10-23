from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()


class ClienteInput(BaseModel):

    spending: float

    advance_payments: float

    probability_of_full_payment: float

    current_balance: float

    credit_limit: float

    min_payment_amt: float

    max_spent_in_single_shopping: float

    porcentaje_credito_usado: float

    ratio_pago: float


@app.get("/health")
def health():

    return {

        "status": "ok"

    }


@app.post("/predecir")
def predecir(data: ClienteInput):

    payload = {

        "dataframe_records": [

            data.dict()

        ]

    }

    headers = {

        "Authorization":
        f"Bearer {os.getenv('DATABRICKS_TOKEN')}",

        "Content-Type":
        "application/json"

    }

    response = requests.post(

        os.getenv("DATABRICKS_URL"),

        headers=headers,

        json=payload

    )

    return response.json()
