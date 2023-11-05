from fastapi import FastAPI
import torch
from pydantic import BaseModel


class RequestBody(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/process-transaction")
async def process_transaction(req: RequestBody):
    return req

@app.post("/tbd")
async def tbd():
    return {"message": "Hello World"}