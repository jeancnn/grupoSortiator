from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def root():
    return "TESTE"