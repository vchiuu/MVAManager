from flask import render_template, Blueprint, current_app
from mvaManager import db, bcrypt, mail

tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks')
def taskslist():
  return render_template('tasks.html', title='Tasks')