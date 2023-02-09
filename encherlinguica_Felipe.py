from database import engine
from sqlmodel import Session, select
from models.model import ClassRoom, Student, Group
from sqlalchemy.orm import selectinload
from controller.students_controller import findStudent, createStudent, editStudent, deleteStudent


while True:
    print("Escolha uma das opções: ")
    print("\n 1 - Buscar Alunos:\n 2 - Criar aluno\n 3 - Editar Aluno\n 4 - Deletar Aluno\n Digite qualquer outro número para sair.\n")
    match input(" > "):
        case "1":
            findStudent()
        case "2":
            createStudent(input("Informe o ID da sala: "))
        case "3":
            #aluno_editado = (Student(name=input('Nome do Aluno: '), contact=input('Contato:')))
            editStudent(input("Informe o ID do Aluno para Editar: "),dadosAluno=(Student(name=input('Nome do Aluno: '), contact=input('Contato:'))))

        case "4":
            deleteStudent(input("Informe o ID do Aluno para deletar: "))
        case _:
            break


