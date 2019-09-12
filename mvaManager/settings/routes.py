
from flask import render_template, url_for, flash, redirect, request, Blueprint
from mvaManager import db
from mvaManager.settings.forms import newPractitionerForm
from mvaManager.models import Practitioner, AppointmentSchedule
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

settings = Blueprint('settings', __name__)

@settings.route('/settings')
def settings_dir():
  return render_template('settings.html', title="Settings")

@settings.route('/settings/practitioners')
def practitioners():
  practitioners = Practitioner.query.all()
  return render_template('practitioners/practitioners.html', title="Practitioners", practitioners=practitioners)

@settings.route('/settings/addpractitioner', methods=['GET', 'POST'])
def addpractitioner():
  form = newPractitionerForm()
  if form.validate_on_submit():
    practitioner = Practitioner(firstName = form.firstName.data, lastName = form.lastName.data, 
                                practice = form.practice.data, certificateNumber = form.certificateNumber.data)
    db.session.add(practitioner)
    db.session.commit()
    flash('Practitioner sucessfully added!', 'success')
    return redirect( url_for('settings.practitioners') )
  return render_template('practitioners/addpractitioner.html', title="Add Practitioner", form=form)

@settings.route('/settings/<int:practitioner_id>')
def practitioner(practitioner_id):
  practitioner = Practitioner.query.get_or_404(practitioner_id)
  return render_template('practitioners/practitioner.html', title="Practitioner", practitioner=practitioner)

@settings.route('/practitioners/<int:practitioner_id>/update', methods=['GET', 'POST'])
@login_required
def updatepractitioner(practitioner_id):
  practitioner = Practitioner.query.get_or_404(practitioner_id)
  form = newPractitionerForm()
  if form.validate_on_submit():
    practitioner.firstName = form.firstName.data
    practitioner.lastName = form.lastName.data
    practitioner.practice = form.practice.data
    practitioner.certificateNumber = form.certificateNumber.data
    db.session.commit()
    flash('Practitioner information has been updated', 'success')
    return redirect( url_for('settings.practitioner', practitioner_id=practitioner.id))
  elif request.method == 'GET':
    form.firstName.data = practitioner.firstName
    form.lastName.data = practitioner.lastName
    form.practice.data = practitioner.practice
    form.certificateNumber.data = practitioner.certificateNumber
  return render_template('practitioners/addpractitioner.html', title='Update Practitioner', form=form, legend='Update Practitioner')

@settings.route('/practitioner/<int:practitioner_id>/delete', methods=['POST'])
@login_required
def deletepractitioner(practitioner_id):
  practitioner = Practitioner.query.get_or_404(practitioner_id)
  db.session.delete(practitioner)
  db.session.commit()
  flash('Practitioner has been deleted', 'success')
  return redirect(url_for('settings.practitioners'))

@settings.route('/settings/appointmentschedule')
@login_required
def appointmentschedule():
  appointmentschedule = AppointmentSchedule.query.all()
  return render_template(
    'servicesfees/apptschedule.html', 
    title="Appointment Schedule", 
    appointmentschedule=appointmentschedule)