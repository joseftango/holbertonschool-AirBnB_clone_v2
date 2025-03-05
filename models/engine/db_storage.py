#!/usr/bin/python3
"""This module defines a class to manage database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    """This class manages storage of
    hbnb models in mysql server"""
    __engine = None
    __session = None

    classes = {
               'State': State, 'City': City, 'User': User,
               'Place': Place, 'Review': Review, 'Amenity': Amenity
              }

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        self.reload()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in DB storage"""
        result = {}
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)

        if cls is None:
            for v in self.classes.values():
                objs = self.__session.query(v).all()
                for obj in objs:
                    for k in obj.__dict__.keys():
                        if '_sa_instance' in k:
                            unneeded_key = k
                    del obj.__dict__[unneeded_key]
                    result[f'{type(obj).__name__}.{obj.id}'] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                result[f'{type(obj).__name__}.{obj.id}'] = obj

        return result

    def new(self, obj):
        """Adds new object to DB storage"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from from table in DB"""
        if obj is None:
            return None
        self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from DB"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        '''call remove() method on the
        private session attribute'''
        self.__session.close()
