from database import engine
from sqlmodel import Session
from models.model import ClassRoom

def cadastraClass():
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=input("Nome do grupo: "))
        session.add(new_class)
        session.commit()
        session.refresh(new_class)
        print(new_class)
        
        
        
cadastraClass()