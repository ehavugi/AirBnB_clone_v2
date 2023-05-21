#!/usr/bin/python3
"""
    New engine DB storage
"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.place import Place
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage instantiation method"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                     user, passwd, host, db),
                                     pool_pre_ping=True)
        self.__session = sessionmaker(bind=self.__engine)()

    def all(self, cls=None):
        """Query on current db session all objects"""
        d = {}
        if cls and isinstance(cls, str):
            cls = eval(cls)
            objects = self.__session.query(cls)
            for obj in objects:
                k = "{}.{}".format(obj.__class__.__name__, obj.id)
                d[k] = obj
            return d

        for obj in [User, State, City, Place, Amenity, Review]:
            objects = self.__session.query(obj).all()
            for obj in objects:
                k = "{}.{}".format(obj.__class__.__name__, obj.id)
                d[k] = obj
        return d

    def save(self):
        """Commit all changes of the current database"""
        self.__session.commit()

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables in database and creates current database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """Remove session"""
        self.reload()
        self.__session.close()
