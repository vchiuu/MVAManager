from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from mvaManager.models import User

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
