from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(128), nullable=False)
    job = Column(String(50), nullable=True)

    # command = relationship("Command", back_populates="")
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, role={self.role})>"


# class Command(Base):
#     __tablename__ = 'commands'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     description = Column(String(255), nullable=False)
