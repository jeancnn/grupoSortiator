from fastapi import FastAPI
from database import engine

app = FastAPI()

from routes.classroom_routes import *


@app.get("/")
def root():
    return "TESTE"