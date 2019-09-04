from flask import render_template, url_for, flash, redirect, request, Blueprint
from mvaManager import db
from mvaManager.patients.forms import newPatientForm
from mvaManager.models import Patient

patients = Blueprint('patients', __name__)

@patients.route('/patients')
def patientslist():
  patientslist = Patient.query.all()
  return render_template('patients.html', title='Patients', patients=patientslist)

@patients.route('/patients/addPatient', methods=['GET', 'POST'])
def addPatient():
  form = newPatientForm()
  if form.validate_on_submit():
    patient = Patient(pFirstName = form.pFirstName.data, pLastName= form.pLastName.data, pDOB=form.pDOB.data, 
      pIncidentDate=form.pIncidentDate.data, pClaimNumber=form.pClaimNumber.data, pScheduleID=form.pScheduleID.data)
    db.session.add(patient)
    db.session.commit()
    flash('Patient has been added.', 'success')
    return redirect( url_for('patients.patientslist'))
  return render_template('addpatient.html', title='AddPatient', form=form)