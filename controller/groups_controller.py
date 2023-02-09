from database import engine
from models.model import ClassRoom, Group

from sqlmodel import Session
from sqlmodel import select

from sqlalchemy.orm import selectinload

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



### Cadastrar uma sala/classe
# Isso é apenas um ex, ainda não está pronto
def cadastraGrupo(classRoom:Group):
    with Session(engine) as session:
        new_group = Group(id=None, name=classRoom.name)
        session.add(new_group)
        session.commit()
        session.refresh(new_group)
        return new_group


def buscaGruposClasse(classID):
    with Session(engine) as session:
        statement = select(Group).where(Group.id_classroom == classID).options(selectinload(Group.classroom))
        results = session.exec(statement).all()
        print(results)
        
        return str(results)
        #return JSONResponse(content=jsonable_encoder(results))