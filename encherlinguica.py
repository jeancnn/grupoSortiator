from database import engine
from sqlmodel import Session, select
from models.model import ClassRoom, Student
from sqlalchemy.orm import selectinload

def cadastraClass():
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=input("Nome do grupo: "))
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)

def cadastrarStudent(idClassRoom):
    with Session(engine) as session:
        new_class = Student(id=None, name=input("Nome do aluno: "), contact="asdasd@asdasd.com", id_classroom=idClassRoom)
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

#cadastraClass()

#cadastrarStudent(2)

buscaClasseAlunos()

