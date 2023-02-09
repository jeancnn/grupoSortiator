from controller.students_controller import findStudent,createStudent,editStudent,deleteStudent

from main import app

@app.get("/student")
def busca_aluno():
    return findStudent()

@app.post("/student")
def classroom():
    pass