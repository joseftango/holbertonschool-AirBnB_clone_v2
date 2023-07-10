#!/usr/bin/python3
"""db_storage module that defines DBStorage class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """class named DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """constractor method"""

        self.__engine = create_engine('mysql+mysqlconnector://{}:{}\
@{}:3306/{}'.format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                         pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """method that query on the current database session
        all objects depending of the class name"""
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
        query = []
        if cls:
            query = self.__session.query(cls).all()
        else:
            objs = [State, City, User, Place, Review]
            for o in objs:
                query.extend(self.__session.query(o).all())

        obj_to_dict = dict()
        for o in query:
            obj_to_dict[f'{o.__class__.__name__}.{o.id}'] = o
        return obj_to_dict

    def new(self, obj):
        """add the object to the
        current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to
        the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database
        session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database and
        creates the current database session"""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(s)

    def close(self):
        """method that close the session"""
        self.__session.close()
