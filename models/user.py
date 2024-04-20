#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", back_populates='user',
                          cascade="all, delete, delete-orphan")

    reviews = relationship("Review", back_populates='user',
                           cascade="all, delete, delete-orphan")
