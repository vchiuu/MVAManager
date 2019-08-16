from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registrationForm(FlaskForm):
  username = StringField('userName', validators=[DataRequired(), Length(min=8, max=16)])
  email = StringField('email', validators=[DataRequired(), Email()])
  password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
  confirmPassword = PasswordField('confirmPassword', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

class loginForm(FlaskForm):
  username = StringField('userName', validators=[DataRequired(), Length(min=8, max=16)])
  password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
  remember = BooleanField('rememberMe')
  submit = SubmitField('Sign In')