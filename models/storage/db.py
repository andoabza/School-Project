""" for the database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.model import ModelBase, Base
from models.student import Student



classes = {"Student": Student}
class DbStorage:
    """for the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the database storage"""
        user = 'anda'
        paswd = 'root'
        host = 'localhost'
        db = 'school_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user,
                                             paswd,
                                             host,
                                             db))

    def all(self, cls=None):
        """returns a dictionary of all objects"""
        new_dict = {}
        if cls is None:
            classes = [Student]
        else:
            classes = [cls]
        for cls in classes:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """adds the object to the current database session"""
        rec = self.__session.query(obj.__class__).filter_by(first_name=obj.first_name, last_name=obj.last_name).first()
        if rec is not None:
            self.__session.merge(rec)
        else:
            self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None"""
        
        if obj is not None:
            rec = self.__session.query(obj.__class__).filter_by(first_name=obj.first_name, last_name=obj.last_name).first()
            self.__session.delete(rec)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """calls remove() method on the private session attribute"""
        self.__session.remove()
    
    def get(self, cls=None):
        """returns the object based on the class name and its ID,
        or None if not found"""
        if cls  not in classes.values():
            return None
        else:
            return self.__session.query(cls).all()
