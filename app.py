from models.student import Student
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.strict_slashes = False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        middle_name = request.form['middle_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        grade = request.form['grade']
        student = Student(first_name=first_name, last_name=last_name, middle_name=middle_name, grade=grade)
        student.save()
        return "Student registered!"
    return render_template('register.html')

app.run()


