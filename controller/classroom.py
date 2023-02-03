from database import engine
from models.model import ClassRoom

from sqlmodel import Session
from sqlmodel import select

from sqlalchemy.orm import selectinload

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



### Cadastrar uma sala/classe
# Isso é apenas um ex, ainda não está pronto
def cadastraClass(classRoom:ClassRoom):
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=classRoom.name)
        session.add(new_class)
        session.commit()
        session.refresh(new_class)
        return new_class


def buscaClasseAlunos():
    with Session(engine) as session:
        statement = select(ClassRoom).options(selectinload(ClassRoom.students))
        results = session.exec(statement).all()
        print(results)
        
        return str(results)
        #return JSONResponse(content=jsonable_encoder(results))