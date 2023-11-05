from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
        "http://localhost:9000",
        "http://localhost:8000",
        "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    userid: str
    amount: float
    propertyid: str

class CredsRequestBody(BaseModel):
    email: str
    password: float

class DummyRequestBody(BaseModel):
    req: str



@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.post("/buy/")
async def process_buy(req: RequestBody):
    return req

@app.post("/sell/")
async def process_sell(req: RequestBody):
    return req

@app.post("/register")
async def process_register(req: str):
    return {"message": req}

@app.post("/value")
async def process_value(req: DummyRequestBody):
    print(req)
    return {"message": req}
