from fastapi import FastAPI
from database import engine

app = FastAPI()

from views.classroom import *


@app.get("/")
def root():
    return "TESTE"