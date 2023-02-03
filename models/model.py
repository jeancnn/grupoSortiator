from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


class ClassRoom(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    
    students: List["Student"] = Relationship(back_populates="classroom")
    groups: List["Group"] = Relationship(back_populates="classroom")
    


class Group(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False, index=True)
    description: str = Field()
    
    id_classroom: Optional[int] = Field(default=None, foreign_key="classroom.id")
    classroom: Optional[ClassRoom] = Relationship(back_populates="groups")
    
    students: List["Student"] = Relationship(back_populates="group")
    
    


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    contact: str = Field(index=True)

    id_classroom: Optional[int] = Field(default=None, foreign_key="classroom.id")
    classroom: Optional[ClassRoom] = Relationship(back_populates="students")

    id_group: Optional[int] = Field(default=None, foreign_key="group.id")
    group: List["Group"] = Relationship(back_populates="students")


