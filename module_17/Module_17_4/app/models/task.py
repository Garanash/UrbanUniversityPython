from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.backend.db import Base
from app.models.user import User


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    slug = Column(String, unique=True, index=True)
    _user = relationship('User', backref='tasks')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))
