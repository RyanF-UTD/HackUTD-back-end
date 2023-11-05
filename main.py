from fastapi import FastAPI
#import torch
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
async def process_transaction(req: RequestBody):
    return req

@app.post("/sell")
async def process_transaction(req: RequestBody):
    return req

@app.post("/register")
async def process_transaction(req: str):
    return {"message": req}

@app.post("/value")
async def process_transaction(req: str):
    return {"message": req}

@app.post("/login")
async def login(user: User):
    # Here you can add your logic to check if the email and password are valid
    # For example, you can check if the email exists in your database and if the password matches
    # If the email and password are valid, you can return a success message
    # If the email or password are invalid, you can return an error message
    return {"message": "Login successful"}