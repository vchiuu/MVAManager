from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mvaManager.models import Patient

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
