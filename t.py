def register():
    if request.method == 'POST':
        Id = request.form['id']
        middle_name = request.form['middle_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        grade = request.form['grade']
        student = Student(student_id=Id, first_name=first_name.upper(), last_name=last_name.upper(), middle_name=middle_name.upper(), gender=gender, grade=grade)
        record = storage.get(Id)
        if not  record:
            storage.new(student)
            storage.save()
            flash('Student registered successfully')