from flask import render_template, Blueprint
from mvaManager import app, db, bcrypt, mail

tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks')
def taskslist():
  return render_template('tasks.html', title='Tasks')