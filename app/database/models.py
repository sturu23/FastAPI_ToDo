from sqlalchemy import String, Integer, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship
from .db import Base



class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    body = Column(Integer)
    is_active = Column(Boolean,default=True)
