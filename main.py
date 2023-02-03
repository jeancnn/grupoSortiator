from fastapi import FastAPI
from database import engine

from views.classroom import *

app = FastAPI()

@app.get("/")
def root():
    return "TESTE"