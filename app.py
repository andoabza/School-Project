from models import storage
from models.student import Student
from flask import Flask, render_template, request, make_response


app = Flask(__name__)
app.strict_slashes = False

@app.teardown_appcontext
def close_db(error):
        storage.close()

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        middle_name = request.form['middle_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        grade = request.form['grade']
        student = Student(first_name=first_name, last_name=last_name, middle_name=middle_name, gender=gender, grade=grade)
        student.save()
        return "Student registered!"
    return render_template('register.html')

app.run()


