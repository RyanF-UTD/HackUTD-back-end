from fastapi import FastAPI
import torch


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
