from models.student import Student
from models import storage
student = Student(id='102', name='ando')
re = storage.all()

if student.id in re:
    print("Student already exists")
print(re)
# from models.student import Student
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session

# user = 'school'

# paswd = 'school_pwd'

# host = 'localhost'

# db = 'school_db'

# engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
#                                         format(user,
#                                                  paswd,
#                                                  host,
#                                                  db))
# session_factory = sessionmaker(bind=engine,
#                                         expire_on_commit=False)
# Session = scoped_session(session_factory)

# session = Session()

# rec = session.query(Student).all()

# for r in rec:
#     if '_sa_instance_state' in r.__dict__:
#         del r.__dict__['_sa_instance_state']
#     print(r.__dict__)


# import MySQLdb

# # Open database connection
# db = MySQLdb.connect("localhost","school","school_pwd","school_db" )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # execute SQL query using execute() method.
# rec = cursor.execute("SELECT * FROM students")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()

# column_names = [column[0] for column in cursor.description]
# data = [dict(zip(column_names, row)) for row in data]

# print(data)
