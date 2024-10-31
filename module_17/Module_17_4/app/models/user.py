from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.backend.db import Base
# from app.models.task import Task


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    _tasks = relationship('Task', backref='users')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))
