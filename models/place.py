#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review


class Place(BaseModel, Base):
	""" A place to stay """
	__tablename__ = "places"
	if getenv('HBNB_TYPE_STORAGE') == 'db':
		city_id = Column("city_id", String(60), ForeignKey('cities.id') , nullable=False)
		user_id = Column("user_id", String(60), ForeignKey('users.id'), nullable=False)
		name = Column("name", String(128), nullable=False)
		description = Column("description", String(1024), nullable=True)
		number_rooms = Column("number_rooms", Integer, default=0, nullable=False)
		number_bathrooms = Column("number_bathrooms", Integer, default=0, nullable=False)
		max_guest = Column("max_guest", Integer, default=0, nullable=False)
		price_by_night = Column("price_by_night", Integer, default=0, nullable=False)
		latitude = Column("latitude", Float, nullable=True)
		longitude = Column("longitude", Float, nullable=True)
		amenity_ids = []
		reviews = relationship("Review", backref="place", cascade="all, delete")
	else:
		city_id = ""
		user = ""
		name = ""
		description = ""
		number_rooms = 0
		number_bathrooms = 0
		max_guest = 0
		price_by_night = 0
		latitude = 0.0
		longitude = 0.0
		amenity_ids = []

		@property
		def reviews(self):
			"""returns the list of Review instances with
			place_id equals to the current Place.id"""
			list_rev = {}
			for v in models.storage.all(Review).values():
				if self.id == v.place_id:
					list_rev.append(v)
			return list_rev
