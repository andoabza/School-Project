""" a model that will create a user, get a user, update a user, and delete a user """
from sqlalchemy import  Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import storage

Base = declarative_base()
class ModelBase:
    """the base classs for students"""
    
    Time = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("Time", None) and type(self.Time) is str:
                self.Time = datetime.strptime(kwargs["Time"], time)
            else:
                self.Time = datetime.utcnow()
        else:
            self.Time = datetime.utcnow()
    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.Time = datetime.utcnow()
        storage.new(self)
        storage.save()
    
    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}]  {}".format(self.__class__.__name__,
                                         self.__dict__)
   