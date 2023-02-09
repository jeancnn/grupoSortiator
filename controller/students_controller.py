from database import engine
from sqlmodel import Session, select
from models.model import  Student
from sqlalchemy.orm import selectinload
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def findStudent():
    with Session(engine) as session:
        statement = select(Student)
        results = session.exec(statement).all()
        print(results)

def createStudent(idClassRoom,student:Student):
    with Session(engine) as session:
        new_class = Student(id=None, name=student.name, contact=student.contact, id_classroom=idClassRoom)
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)

def editStudent(studentID, dadosAluno: Student):
    with Session(engine) as session:
        statement = select(Student).where(Student.id == studentID)
        results = session.exec(statement).first()
        results.name = dadosAluno.name
        results.contact = dadosAluno.contact

        session.add(results)
        session.commit()
        session.refresh(results)
        print(results)
        return JSONResponse(content=jsonable_encoder(results))

def deleteStudent(studentID):
    with Session(engine) as session:
        statement = select(Student).where(Student.id == studentID)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()
        
        return print('Deleted Student')


