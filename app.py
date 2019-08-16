from flask import Flask, render_template, url_for
from forms import registrationForm, loginForm

# name of the current module which is app.py
app = Flask(__name__) 
# secret key for your cookie session
app.config['SECRET_KEY'] = ' 23456787654321234563'
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

@app.route('register')
def registration():
  form = registrationForm()
  return render_template('register.html', title='Register', form=form)

@app.route('login')
def login():
    form = loginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/<name>')
def name(name):
  return '<h1> Hello {}! </h1>'.format(name)
