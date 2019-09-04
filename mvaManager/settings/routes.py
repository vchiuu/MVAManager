
from flask import render_template, url_for, flash, redirect, request, Blueprint
from mvaManager import db
from mvaManager.settings.forms import newPractitionerForm
from mvaManager.models import Practitioner
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

settings = Blueprint('settings', __name__)

@settings.route('/settings')
def settings_dir():
  return render_template('settings.html', title="Settings")

@settings.route('/settings/practitioners')
def practitioners():
  practitioners = Practitioner.query.all()
  return render_template('practitioners.html', title="Practitioners", practitioners=practitioners)

@settings.route('/settings/addpractitioner')
def addpractitioner():
  form = newPractitionerForm()
  if form.validate_on_submit():
    practitioner = Practitioner(firstName = form.firstName.data, lastName = form.lastName.data, 
                                practice = form.practice.data, claimNumber = form.claimNumber.data)
    db.session.add(practitioner)
    db.session.commit()
    flash('Practitioner sucessfully added!', 'success')
    return redirect( url_for('settings.practitioners') )
  return render_template('addpractitioner.html', title="Add Practitioner", form=form)

@settings.route('/settings/<int:practitioner_id>')
def practitioner(practitioner_id):
  practitioner = Practitioner.query_get_or_404(practitioner_id)
  return render_template('practitioner.html', title="Practitioner", practitioner=practitioner)
