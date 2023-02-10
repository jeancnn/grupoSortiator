from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel


class ClassRoom(SQLModel, BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    
    students: List["Student"] = Relationship(back_populates="classroom")
    groups: List["Group"] = Relationship(back_populates="classroom")
    
    class Config:
        orm_mode = True
    


class Group(SQLModel,BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False, index=True)
    description: str = Field()
    
    id_classroom: Optional[int] = Field(default=None, foreign_key="classroom.id")
    classroom: Optional[ClassRoom] = Relationship(back_populates="groups")
    
    students: List["Student"] = Relationship(back_populates="group")
    
    class Config:
        orm_mode = True
    
    

class Student(SQLModel,BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    contact: str = Field(index=True)

    id_classroom: Optional[int] = Field(default=None, foreign_key="classroom.id")
    classroom: Optional[ClassRoom] = Relationship(back_populates="students")

    id_group: Optional[int] = Field(default=None, foreign_key="group.id")
    group: List["Group"] = Relationship(back_populates="students")

    class Config:
        orm_mode = True

