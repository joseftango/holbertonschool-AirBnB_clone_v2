#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              back_populates="state",
                              cascade="all, delete")
    else:
        name = ''
        @property
        def cities(self):
            '''returns the list of City instances with
            state_id equals to the current State.id'''
            all_cities = models.storage.all(City)
            matches_cities = []

            for v in all_cities.values():
                if self.id == v.state_id:
                    matches_cities.append(v)

            return matches_cities
