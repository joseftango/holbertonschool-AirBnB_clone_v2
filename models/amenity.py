#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """class named Amenity"""
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column("name", String(128), nullable=False)
    else:
        name = ""
