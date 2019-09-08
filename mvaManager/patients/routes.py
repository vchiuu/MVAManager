from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from mvaManager import db
from mvaManager.patients.forms import newPatientForm
from mvaManager.models import Patient, BillingSchedule
import datetime

patients = Blueprint('patients', __name__)

@patients.route('/patients')
def patientslist():
  patientslist = Patient.query.all()
  return render_template('patients/patients.html', title='Patients', patients=patientslist)

@patients.route('/patients/addPatient', methods=['GET', 'POST'])
def addPatient():
  form = newPatientForm()
  if form.validate_on_submit():
    patient = Patient(
      pFirstName = form.pFirstName.data, 
      pLastName= form.pLastName.data, 
      pDOB=form.pDOB.data, 
      pPhone=form.pPhone.data, 
      pEmailAddress=form.pEmailAddress.data, 
      pIncidentDate=form.pIncidentDate.data,
      pClaimNumber=form.pClaimNumber.data, 
      pScheduleID=form.pScheduleID.data, 
      pNotes=form.pNotes.data)
    db.session.add(patient)
    db.session.commit()
    flash('Patient has been added.', 'success')
    return redirect( url_for('patients.patientslist'))
  return render_template('patients/addpatient.html', title='AddPatient', form=form)

@patients.route('/patients/<int:patient_id>')
def patient(patient_id):
  patient = Patient.query.get_or_404(patient_id)
  schedules = BillingSchedule.query.get(patient_id)
  return render_template('patients/patient.html',
    title=(patient.pFirstName + patient.pLastName),
    patient=patient, billingschedules=schedules)

@patients.route('/patients/<int:patient_id>/update', methods=['GET', 'POST'])
@login_required
def updatepatient(patient_id):
  patient = Patient.query.get_or_404(patient_id)
  form = newPatientForm()
  if form.validate_on_submit():
    patient.pFirstName = form.pFirstName.data
    patient.pLastName = form.pLastName.data
    patient.pDOB = form.pDOB.data
    patient.pPhone = form.pPhone.data
    patient.pEmailAddress = form.pEmailAddress.data
    patient.pIncidentDate = form.pIncidentDate.data
    patient.pClaimNumber = form.pClaimNumber.data
    patient.pScheduleID = form.pScheduleID.data
    patient.pNotes = form.pNotes.data
    db.session.commit()
    flash('Patient information has been updated', 'success')
    return redirect( url_for('patients.patient', patient_id=patient.id))
  elif request.method == 'GET':
    form.pFirstName.data = patient.pFirstName
    form.pLastName.data = patient.pLastName
    form.pDOB.data = patient.pDOB
    form.pPhone.data = patient.pPhone
    form.pEmailAddress.data = patient.pEmailAddress
    form.pIncidentDate.data = patient.pIncidentDate
    form.pClaimNumber.data = patient.pClaimNumber
    form.pScheduleID.data = patient.pScheduleID
    form.pNotes.data = patient.pNotes
  return render_template('patients/addpatient.html', title='Update Patient', form=form, legend='Update Patient')

@patients.route('/patients/<int:patient_id>/addbillingschedule', methods=['POST'])
@login_required
def addbillingschedule(patient_id):
  patient = Patient.query.get_or_404(patient_id)
  billingschedule = BillingSchedule (
    endBlock1 = patient.pIncidentDate + datetime.timedelta(days=28), 
    endBlock2 = patient.pIncidentDate + datetime.timedelta(days=56),
    endBlock3 = patient.pIncidentDate + datetime.timedelta(days=84), 
    patient_id = patient.id
  )
  db.session.add(billingschedule)
  db.session.commit()
  return redirect( url_for('patients.patient', patient_id = patient.id))
  
@patients.route('/patients/<int:patient_id>/delete', methods=['POST'])
@login_required
def deletepatient(patient_id):
  billingschedule = BillingSchedule.query.get_or_404(patient_id)
  db.session.delete(billingschedule)
  patient = Patient.query.get_or_404(patient_id)
  db.session.delete(patient)
  db.session.commit()
  flash('Patient has been deleted', 'success')
  return redirect(url_for('patients.patientslist'))
  