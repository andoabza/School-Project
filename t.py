from save.file_save import save_to_excel

from models.student import Student
from models import storage

record = storage.all()

save_to_excel(record)


# from flask import Flask
# from flask_mail import Mail, Message

# app = Flask(__name__)
# mail= Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'andaabi3@mail.com'
# app.config['MAIL_PASSWORD'] = '28303235@anda'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

# def index():
#    msg = Message('Hello', sender = 'andaabi3@gmail.com', recipients = ['terbu102@gmail.com'])
#    msg.body = "Hello Flask message sent from Flask-Mail"
#    mail.send(msg)
#    return "Sent"
# index()