from fastapi import FastAPI
from fastapi import status
from database import engine

app = FastAPI(
    title='Grupo sortiator tabajara',
    description='API de criação de salas e sorteio de usuários em grupos dentro de classe',
    version='0.001beta',
    contact={
        "name": "Equipe os Confirmados",
        "email": "elvis.o.rei@bluesuedshoes.com"
        }
    )

from routes import all_routes


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return "Welcome"