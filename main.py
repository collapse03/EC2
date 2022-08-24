from http.client import HTTPException
import json
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PreselectaItem(BaseModel):
    idNumber: str
    idType: str
    firstLastName: str
    inquiryClientId: str
    inquiryUserId: str
    inquiryUserType: str
    inquiryParameters: list[dict]

@app.post("/preselecta")
def ConsumoPreselecta(json_in: PreselectaItem):
    json_in_convert = json_in.dict()
    urlApiGatewayPreselecta = 'https://s3erc6n2bf.execute-api.us-east-1.amazonaws.com/dev/preselecta'

    try:
        reponse = requests.post(urlApiGatewayPreselecta, json.dumps(json_in_convert))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error al realizar la consulta con el servicio de Experian access token")
    return reponse.json()