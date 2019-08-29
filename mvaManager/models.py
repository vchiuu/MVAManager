from datetime import datetime
from mvaManager import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)
  
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
  patientID = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String, nullable=False)
  lastName = db.Column(db.String, nullable=False)
  dateofBirth = db.Column(db.DateTime, nullable=False)
  dateofAccident = db.Column(db.DateTime, nullable=False)
  claimNumber = db.Column(db.String, nullable=False)
  appointments = db.relationship('Appointment', backref='patient', lazy=True)

class Appointment(db.Model):
   appointmentID = db.Column(db.Integer, primary_key=True)
   appointmentDate = db.Column(db.DateTime, nullable=False)
   treatment = db.Column(db.String(20), nullable=False)

class Treatment(db.Model):
  treatmentID = db.Column(db.Integer, primary_key=True)
  trtType = db.Column(db.Integer, priamry_key=True)
