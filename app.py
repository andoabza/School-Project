import models
from models import storage
from models.student import Student
from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)
app.strict_slashes = False
app.secret_key = 'some_secret'

@app.teardown_appcontext
def close_db(error):
        storage.close()

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/new', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        Id = request.form['id']
        
        middle_name = request.form['middle_name']
        
        first_name = request.form['first_name']
        
        last_name = request.form['last_name']
        
        gender = request.form['gender']
        
        grade = request.form['grade']
        
        student = Student(student_id=Id, first_name=first_name, last_name=last_name, middle_name=middle_name, gender=gender, grade=grade)
        
        record = storage.all()
        
        if student.student_id not in record:
        
            storage.new(student)
        
            storage.save()
        
            flash('Student registered successfully')
            return redirect(url_for('index'))
        else:
            flash('Student with this id already exists')
        
    return render_template('register.html')

app.run(debug=True)


