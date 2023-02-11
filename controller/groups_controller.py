from database import engine
from models.model import ClassRoom, Group

from sqlmodel import Session
from sqlmodel import select

from sqlalchemy.orm import selectinload

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status


def findGroupsClassroom(classID: int = None):
    with Session(engine) as session:
        statement = select(Group).where(Group.id_classroom == classID).options(selectinload(Group.classroom))
        results = session.exec(statement).all()
        print(results)
        
        return JSONResponse(content=jsonable_encoder(results))


def createGroup(classRoom:Group):
    with Session(engine) as session:
        new_group = Group(id=None, name=classRoom.name)
        session.add(new_group)
        session.commit()
        session.refresh(new_group)

        return JSONResponse(content=jsonable_encoder(new_group))

def editGroup(groupID, classRoom:Group):
    with Session(engine) as session:
        statement = select(Group).where(Group.id == groupID)
        results = session.exec(statement).first()

        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail= {"message": f"No group found with id: {groupID}"}
            )
        else:
            results.name = classRoom.name
            results.description = classRoom.description

            session.add (results)
            session.commit()
            session.refresh(results)
            print(results)
            return JSONResponse(content=jsonable_encoder(results))

def deleteGroup(groupID):
    with Session(engine) as session:
        statement = select(Group).where(Group.id == groupID)
        results = session.exec(statement).first()
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail= {"message": f"No group found with id: {groupID}"}
            )
        else:
            session.delete(results)
            session.commit()
            # Falta fazer aqui