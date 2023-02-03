from sqlmodel import SQLModel, create_engine
import models.model

engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)