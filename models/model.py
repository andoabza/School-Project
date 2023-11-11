""" a model that will create a user, get a user, update a user, and delete a user """
from sqlalchemy import  Column,  String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import hashlib
from datetime import datetime
import models

Base = declarative_base()

class ModelBase:
    """the base classs for students"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)    

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                uuid_id = uuid.uuid4()
                # take the first 4 characters of its SHA-1 hash
                short_id = hashlib.sha1(uuid_id.bytes).hexdigest()[:4]
                self.id = str(short_id)
        else:
            uuid_id = uuid.uuid4()
            # take the first 4 characters of its SHA-1 hash
            short_id = hashlib.sha1(uuid_id.bytes).hexdigest()[:4]
            self.id = str(short_id)
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        data = models.storage.all()
        record = models.storage.get(self.__class__.__name__, self.first_name, self.middle_name, self.last_name, self.grade) 
        if record in data:
            print("record exists")
        # if no such record exists, save the new record
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in new_dict.keys():
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        models.storage.delete(self)