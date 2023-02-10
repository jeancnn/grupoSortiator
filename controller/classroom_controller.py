from database import engine
from models.model import ClassRoom

from sqlmodel import Session
from sqlmodel import select

from sqlalchemy.orm import selectinload

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.model import Student
from typing import Optional, List


from fastapi import Response
import json


### Cadastrar uma sala/classe
# Isso é apenas um ex, ainda não está pronto
def cadastraClasse(classRoom:ClassRoom):
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=classRoom.name)
        session.add(new_class)
        session.commit()
        session.refresh(new_class)
        return new_class


def buscaClasseAlunos(classeID: int = None):

    with Session(engine) as session:
        if classeID is None:
            statement = select(ClassRoom).options(selectinload(ClassRoom.students))
            results = session.exec(statement).all()
            return results
            
        else:
            statement = select(Student).where(Student.id_classroom == classeID)
            results = session.exec(statement).all()
            return results