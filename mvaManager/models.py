from flask import current_app
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mvaManager import db, login_manager
from flask_login import UserMixin #--> adds the following for us: isAuthenticated, isActive, isAnonymous, getId

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
  
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  firstname = db.Column(db.String(20), nullable=False)
  lastname = db.Column(db.String(20), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def get_reset_token(self, expires_sec=1800):
    s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')

  @staticmethod
  def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try: 
      user_id = s.loads(token)['user_id']
    except:
      return None
    return User.query.get(user_id)
  
  def __repr__(self):
    return f" User('{self.username}', '{self.email}',  '{self.image_file}' )"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20), nullable=False, default='(New Title)')
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  
  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}') "

class Patient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  pFirstName = db.Column(db.String(20), nullable=False)
  pLastName = db.Column(db.String(20), nullable=False)
  pPhone = db.Column(db.String(20))
  pEmailAddress = db.Column(db.String(35))
  pDOB = db.Column(db.DateTime)
  pIncidentDate = db.Column(db.DateTime, nullable=False)
  pClaimNumber = db.Column(db.Integer, nullable=False)
  pScheduleID = db.Column(db.Integer, unique=True, nullable=False)
  pNotes = db.Column(db.Text)


class Practitioner(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String(20), nullable=False)
  lastName = db.Column(db.String(20), nullable=False)
  practice = db.Column(db.String(20), nullable=False)
  certificateNumber = db.Column(db.String(10), nullable=False)

class TreatmentType(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  trtType = db.Column(db.String(15), primary_key=True)

class AppointmentsByBlock(db.Model):
  blockNumber = db.Column(db.Integer, primary_key=True)
  numofAppointments = db.Column(db.Integer, nullable=False)

class Practice(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  practice = db.Column(db.String(20), nullable=False)

class Appointment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  appointmentDate = db.Column(db.DateTime, nullable=False)

class Paperwork(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  formType = db.Column(db.String(7), nullable=False)
  formName = db.Column(db.String(30), nullable=False)
  isRequired = db.Column(db.Boolean)
  isComplete = db.Column(db.Boolean)

class BillingSchedule(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  endBlock1 = db.Column(db.DateTime)
  endBlock2 = db.Column(db.DateTime)
  endBlock3 = db.Column(db.DateTime)
  extensionID = db.Column(db.Integer)

class ExtendedBillingSchedule(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  amountApproved = db.Column(db.Integer, nullable=False)