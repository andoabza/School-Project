from models.model import ModelBase
ModelBase
ModelBase.to_exel("students.xlsx")


# import pandas as pd
# from models import storage
# from models.student import Student

# # ... your existing code ...

# students_dict = storage.all()

# df = pd.DataFrame.from_records(list(students_dict.values()))
# df.to_excel('students.xlsx', index=False)
# # import csv
# # from models import storage
# # from models.student import Student

# # # ... your existing code ...

# # students_dict = storage.all()
# # if 'Time' in students_dict:
# #     del students_dict['Time']

# # with open('students.csv', 'w', newline='') as csvfile:
# #     fieldnames = ['student_id', 'first_name', 'last_name', 'middle_name', 'gender', 'grade', 'Time']
# #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #     writer.writeheader()
# #     for id, student in students_dict.items():
# #         writer.writerow(student)