from fastapi import FastAPI
import torch
from pydantic import BaseModel


class RequestBody(BaseModel):
    userid: str
    amount: float
    propertyid: str

class CredsRequestBody(BaseModel):
    email: str
    password: float


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/buy")
async def process_buy(req: RequestBody):
    return req

@app.post("/sell")
async def process_sell(req: RequestBody):
    return req

@app.post("/register")
async def process_register(req: str):
    return {"message": req}

@app.post("/value")
async def process_value(req: str):
    return {"message": req}
