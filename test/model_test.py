""" test for user model """
import unittest
from models import storage
from models.student import Student

""" test for user model """
class TestUserModel(unittest.TestCase):
    """ test for user model """
    def setUp(self):
        """ set up"""
        self.student = Student(student_id='002', first_name="Mary",middle_name="Bob", last_name="Dan", gender="Female", grade='11')
        storage.new(self.student)
        storage.save()

    def tearDown(self):
        """ tear down"""
        storage.save()
        storage.close()

    def test_create_user(self):
        """ test that a user is created """
        new_student = Student(student_id='001', first_name="John",middle_name="Terry", last_name="Doe", gender="Male", grade='10')
        storage.new(new_student)
        storage.save()  

    def test_get_user(self):
        retrieved_user = storage.get(Student)
        assert retrieved_user is self.user

if __name__ == '__main__':
    """ main"""
    unittest.main()