from flask import render_template, url_for, flash, redirect
from mvaManager import app
from mvaManager.forms import registrationForm, loginForm
from mvaManager.models import User, Post

posts = [
  {
    'author': 'Vivian Chiu', 
    'title': 'Blog Post 1', 
    'content': 'First Post Content', 
    'date_posted': 'August 12th 2019'
  }, 
  {
    'author': 'John Smith', 
    'title': 'Blog Post 2', 
    'content': 'Second Post Content', 
    'date_posted': 'August 15th 2019'
  }
]


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def registration():
  form = registrationForm()
  if form.validate_on_submit():
    flash(f'Account created for: {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
      if form.username.data == 'flaskuser' and form.password.data == 'flaskpassword':
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
      else:
        flash('Login unsuccessful. Please check username and/or password', 'danger')
    return render_template('login.html', title='Login', form=form)

