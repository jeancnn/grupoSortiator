from controller.classroom import buscaClasseAlunos

from main import app


@app.get("/classroom")
def classroom():
    return buscaClasseAlunos()


