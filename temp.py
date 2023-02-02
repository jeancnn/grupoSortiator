from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    user_name: str = Field(index=True)
    name: str = Field(index=True)
    admin: bool = Field(nullable=True)
    password: str = Field(nullable=False)

    events: List["Event"] = Relationship(back_populates="users")

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    data_event: str = Field(nullable=False)
    title: str = Field(nullable=False, index=True)
    description: str = Field()
    public: bool = Field(default=False)
    active: bool = Field(default=True)
    
    id_user: Optional[int] = Field(default=None, foreign_key="user.id")
    users: Optional[User] = Relationship(back_populates="events")