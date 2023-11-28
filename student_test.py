"""unittests for student model."""
import unittest
from models.student import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = 'school'
paswd = 'school_pwd'
host = 'localhost'
db = 'school_db'
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(user,
                                                paswd,
                                                host,
                                                db))
    
Session = sessionmaker(bind=engine)

class TestStudentModel(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_student_creation(self):
        """Test creating a new student."""
        # Create a new student
        new_student = Student(
            student_id='01',
            first_name='John',
            middle_name='William',
            last_name='Doe',
            gender='Male',
            grade=10
        )

        self.session.add(new_student)
        self.session.commit()

        retrieved_student = self.session.query(Student).filter_by(student_id='01').first()

        self.assertEqual(retrieved_student.first_name, 'John')
        self.assertEqual(retrieved_student.last_name, 'Doe')
        self.assertEqual(retrieved_student.grade, 10)

if __name__ == '__main__':
    unittest.main()
