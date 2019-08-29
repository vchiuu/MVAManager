from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)], render_kw ={"placeholder":" Username"})
  firstname = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": " First Name"})
  lastname = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": " Last Name"})
  email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": " Email"})
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)], render_kw={"placeholder": " Password"})
  confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": " Confirm Password"})
  submit = SubmitField('Sign Up')

class loginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)], render_kw={"placeholder": " Username"})
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)], render_kw= {"placeholder": " Password"})
  remember = BooleanField('Remember Me')
  submit = SubmitField('Sign In')