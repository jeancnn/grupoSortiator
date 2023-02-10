from database import engine
from sqlmodel import Session, select
from models.model import  Student
from sqlalchemy.orm import selectinload
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status


def findStudent(studentID: int = None):
    with Session(engine) as session:
        if studentID is None:
            statement = select(Student)
            results = session.exec(statement).all()
        else:
            statement = select(Student).where(Student.id == studentID)
            results = session.exec(statement).first()
            
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail = {"message": "Student not found"}
            )
        return JSONResponse(content=jsonable_encoder(results))


def createStudent(idClassRoom,student:Student):
    with Session(engine) as session:
        new_student = Student(id=None, name=student.name, contact=student.contact, id_classroom=idClassRoom)
        session.add(new_student)
        session.commit()
        #Não sei se esse refresh é necessário
        session.refresh(new_student)
        #talvez aqui precisa de um try catch
        print(new_student)
        return JSONResponse(content=jsonable_encoder(new_student))


def editStudent(studentID, dadosAluno: Student):
    with Session(engine) as session:
        statement = select(Student).where(Student.id == studentID)
        results = session.exec(statement).first()
        
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail = {"message": f"No Student found with id {studentID}"}
            )
        else:
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
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail = {"message": f"No Student found with id: {studentID}"}
            )
        else:
            session.delete(results)
            session.commit()
            #Não sei exatamente o que retornar aqui
            return True


