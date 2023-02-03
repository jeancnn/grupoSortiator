from database import engine
from sqlmodel import Session, select
from models.model import ClassRoom, Student, Group
from sqlalchemy.orm import selectinload

def cadastraClass():
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=input("Nome da Classe: "))
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)

def cadastrarStudent(idClassRoom):
    with Session(engine) as session:
        new_class = Student(id=None, name=input("Nome do aluno: "), contact=input("Contato do aluno: "), id_classroom=idClassRoom)
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)
        
def cadastrarGrupo(idClassRoom):
    with Session(engine) as session:
        new_class = Group(id=None, name=input("Nome do grupo: "), description=input("Descrição do grupo: "), id_classroom=idClassRoom)
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)
        
def buscaClasseAlunos():
    with Session(engine) as session:
        statement = select(ClassRoom).options(selectinload(ClassRoom.students))
        
        results = session.exec(statement).all()
        print(results)
        return results


while True:
    print("Escolha uma das opções: ")
    print("\n 1 - Cadastrar Classe:\n 2 - Cadastrar aluno\n 3 - Cadastrar Grupo\n 4 - Listar tudo\n Digite qualquer outro número para sair.\n")
    match input(" > "):
        case "1":
            cadastraClass()
        case "2":
            cadastrarStudent(input("Informe o ID da sala: "))
        case "3":
            cadastrarGrupo(input("Informe o ID da sala: "))
        case "4":
            buscaClasseAlunos()
        case _:
            break
