from flask import render_template, url_for, flash, redirect
from mvaManager import app, db, bcrypt
from mvaManager.forms import registrationForm, loginForm
from mvaManager.models import User, Post
from flask_login import login_user, current_user, logout_user

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
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('You account has been created! You are now able to login.', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        return redirect(url_for('home'))
      else:
        flash('Login unsuccessful. Please check username and/or password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))

