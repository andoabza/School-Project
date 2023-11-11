# from flask import Flask, render_template
# app = Flask(__name__)
# app.strict_slashes = False

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')
# app.run()
import models
from models.student import Student
s = Student(first_name="barn", middle_name='amede', last_name="Mihai", grade=10)
s.delete(s)
print(s.id)
