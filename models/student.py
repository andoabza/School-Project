"""for the student model"""
from models.model import ModelBase, Base
from sqlalchemy import Column, String, Integer

class Student(ModelBase, Base):
    """the student class"""
    __tablename__ = "students"
    student_id = Column(String(5), nullable=False, primary_key=True)
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)
    grade = Column(Integer, nullable=False)
    
    
    def __init__(self, *args, **kwargs): 
        """initializes the student"""
        super().__init__(*args, **kwargs)