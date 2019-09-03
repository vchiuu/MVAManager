from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mvaManager.models import User, Patient

class registrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)], render_kw ={"placeholder":" Username"})
  firstname = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": " First Name"})
  lastname = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": " Last Name"})
  email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": " Email"})
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)], render_kw={"placeholder": " Password"})
  confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": " Confirm Password"})
  submit = SubmitField('Sign Up')
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('Username already exists. Please select a different username.')
  def validate_email(self, email):
    email = User.query.filter_by(email=email.data).first()
    if email:
      raise ValidationError('Email has already been used. Please use a different email.')

class loginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)], render_kw={"placeholder": " Username"})
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)], render_kw= {"placeholder": " Password"})
  remember = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class updateAccountForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)], render_kw ={"placeholder":" Username"})
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
  firstname = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": " First Name"})
  lastname = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": " Last Name"})
  email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": " Email"})
  submit = SubmitField('Update')
  def validate_username(self, username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('Username already exists. Please select a different username.')
  def validate_email(self, email):
    if email.data != current_user.email:
      email = User.query.filter_by(email=email.data).first()
      if email:
       raise ValidationError('Email has already been used. Please use a different email.')

class requestResetForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  submit = SubmitField('Request Password Reset')
  
  def validate_email(self, email):
    email = User.query.filter_by(email=email.data).first()
    if email is None:
      raise ValidationError('There is no account with that email. Please register first.')

class resetPasswordForm(FlaskForm):
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)], render_kw={"placeholder": " Password"})
  confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": " Confirm Password"})
  submit = SubmitField('Reset Password')

class postForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
  content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "What's on your mind?"})
  submit = SubmitField('Post')

class newPatientForm(FlaskForm):
  pFirstName = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
  pLastName = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
  pPhone = StringField('Phone Number', render_kw={"placeholder": "(123) 456-7890"})
  pEmail = StringField('Email', render_kw={"placeholder": "patient@email.com"})
  pDOB = DateField('Date of Birth', validators=[DataRequired()], format='%d-%m-%Y', render_kw={"placeholder": "DD-MM-YY"})
  pIncidentDate = DateField('Date of Accident', validators=[DataRequired()], format='%d-%m-%Y', render_kw={"placeholder": "DD-MM-YY"})
  pClaimNumber = IntegerField('Claim Number', validators=[DataRequired()])
  pScheduleID = IntegerField('Schedule ID', validators=[DataRequired()], )
  submit = SubmitField('Add Patient')

class newPractitionerForm(FlaskForm):
  firstName = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
  lastName = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
  practice = StringField('Practice', validators=[DataRequired()], render_kw={"placeholder": "Type of Practice"})
  certificateNumber = StringField('Certificate Number', validators=[DataRequired()], render_kw={"placeholder": "Certificate Number"})
  submit = SubmitField('Add Practitioner')