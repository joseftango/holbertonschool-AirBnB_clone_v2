#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column("id", String(60), primary_key=True, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column("updated_at", DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        dict = self.__dict__.copy()
        if dict['_sa_instance_state']:
            del dict['_sa_instance_state']
        return f"[{self.__class__.__name__}] ({self.id}) {dict}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """method that remove the current
        instance from the storage"""
        models.storage.delete(self)
