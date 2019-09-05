from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from mvaManager.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
  app = Flask(__name__) 
  app.config.from_object(Config)

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  from mvaManager.users.routes import users
  from mvaManager.posts.routes import posts
  from mvaManager.main.routes import main
  from mvaManager.settings.routes import settings
  from mvaManager.reports.routes import reports
  from mvaManager.tasks.routes import tasks
  from mvaManager.patients.routes import patients
  from mvaManager.errors.handlers import errors
  app.register_blueprint(users)
  app.register_blueprint(posts)
  app.register_blueprint(main)
  app.register_blueprint(settings)
  app.register_blueprint(reports)
  app.register_blueprint(tasks)
  app.register_blueprint(patients)
  app.register_blueprint(errors)

  return app
