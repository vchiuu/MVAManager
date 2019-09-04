from flask import render_template, Blueprint
from mvaManager import app

reports = Blueprint('reports', __name__)

@reports.route('/reports')
def reportslist():
  return render_template('reports.html', title='Reports')