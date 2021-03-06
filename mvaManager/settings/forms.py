from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mvaManager.models import User, Patient, Practitioner, AppointmentSchedule

class newPractitionerForm(FlaskForm):
  firstName = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
  lastName = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
  practice = StringField('Practice', validators=[DataRequired()], render_kw={"placeholder": "Type of Practice"})
  certificateNumber = StringField('Certificate Number', validators=[DataRequired()], render_kw={"placeholder": "Certificate Number"})
  submit = SubmitField('Add Practitioner')

class newAppointmentScheduleForm(FlaskForm):
  treatmentStage = IntegerField('Treatment Stage', validators=[DataRequired()], render_kw={"placeholder": "Treatment Stage"})
  duration = IntegerField('Duration', validators=[DataRequired()], render_kw={"placeholder": "Duration"})
  numberOfAppointments = IntegerField('Number of Appointments', validators=[DataRequired()], render_kw={"placeholder": "Number of Appointments"})
  submit = SubmitField('Update Block')