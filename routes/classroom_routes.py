from controller.classroom_controller import buscaClasseAlunos

from main import app


@app.get("/classroom")
def classroom():
    return buscaClasseAlunos()

@app.post("/classroom")
def classroom():
    pass
