from database import engine
from models.model import ClassRoom

from sqlmodel import Session
from sqlmodel import select

from sqlalchemy.orm import selectinload

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status


def buscaClasseAlunos():
    with Session(engine) as session:
        statement = select(ClassRoom).options(selectinload(ClassRoom.students))
        results = session.exec(statement).all()
        
        print(results)
        #return str(results)
        #return JSONResponse(content=jsonable_encoder(results))
        #json_str = json.dumps(results, indent=4, default=str)
        #print(json_str)
        #return JSONResponse(content=jsonable_encoder(json_str))
        #return Response(content=json_str, media_type='application/json')
        return results
    
def createClass(classRoom:ClassRoom):
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=classRoom.name)
        session.add(new_class)
        session.commit()
        session.refresh(new_class)
        return new_class
    
def editClass(classID, classRoom:ClassRoom):
    with Session(engine) as session:
        statement = select(ClassRoom).where(ClassRoom.id == classID)
        results = session.exec(statement).first()
        
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail = {"message": f"No Class found with id {classID}"}
            )
        else:
            results.name = classRoom.name

            session.add(results)
            session.commit()
            session.refresh(results)
            print(results)
            return JSONResponse(content=jsonable_encoder(results))

def deleteClass(classID):
    with Session(engine) as session:
        statement = select(ClassRoom).where(ClassRoom.id == classID)
        results = session.exec(statement).first()
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail = {"message": f"No Class found with id: {classID}"}
            )
        else:
            session.delete(results)
            session.commit()
            #Não sei exatamente o que retornar aqui
            return True