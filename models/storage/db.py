""" for the database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.model import Base
from models.student import Student


classes = {"Student": Student}

class DBStorage:
    """for the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the database storage"""
        user = 'school'
        paswd = 'school_pwd'
        host = 'localhost'
        db = 'school_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(user,
                                                paswd,
                                                host,
                                                db))
    def all(self):
        """returns a dictionary of all objects"""
        rec = self.__session.query(Student).all()
        new_dict = {}
        for obj in rec:
            if '_sa_instance_state' in obj.__dict__:
                del obj.__dict__['_sa_instance_state']
            new_dict[obj.student_id] = obj.__dict__
        return new_dict

    def new(self, obj):
        """adds the object to the current database session"""
        
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get(self, student_id):
        """retrieves one object"""
        rec = self.__session.query(Student).filter_by(student_id=student_id).first()
        if rec:
            return rec
        else:
            return None

    def close(self):
        """calls remove() method on the private session attribute"""
        self.__session.close()
