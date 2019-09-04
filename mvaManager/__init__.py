import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__) 
app.config['SECRET_KEY'] = ' 2345ba6c787654321234a5 c63'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.google.mail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from mvaManager.users.routes import users
from mvaManager.posts.routes import posts
from mvaManager.main.routes import main
from mvaManager.settings.routes import settings
from mvaManager.reports.routes import reports
from mvaManager.tasks.routes import tasks
from mvaManager.patients.routes import patients

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(settings)
app.register_blueprint(reports)
app.register_blueprint(tasks)
app.register_blueprint(patients)