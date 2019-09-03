import os 
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from mvaManager import app, db, bcrypt
from mvaManager.forms import registrationForm, loginForm, updateAccountForm, postForm, newPatientForm, newPractitionerForm
from mvaManager.models import User, Post, Patient, Practitioner
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def registration():
  form = registrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, firstname= form.firstname.data, lastname = form.lastname.data, 
                email=form.email.data, password=hashed_password)
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
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('home')) #ternary conditional in python
      else:
        flash('Login unsuccessful. Please check username and/or password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))

def save_picture(form_picture):
  image_name = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_filename = image_name + f_ext
  picture_path = os.path.join(app.root_path, 'static/profile_pictures', 'picture_filename')
  output_size = (125, 125)
  i = Image.open(form_picture)
  i.thumbnail(output_size)
  i.save(picture_path)
  return picture_filename

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
  form = updateAccountForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file = save_picture(form.picture.data)
      current_user.image_file = picture_file
    current_user.username = form.username.data
    current_user.firstname = form.firstname.data
    current_user.lastname = form.lastname.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Your account has been updated.', 'success')
    return redirect( url_for('account') )
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.firstname.data = current_user.firstname
    form.lastname.data = current_user.lastname
    form.email.data = current_user.email
  image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
  return render_template('account.html', title='Account', image_file = image_file, form=form)

# ----------------------------------------------------------------------------------------------
# **************************************** Settings ********************************************
# ----------------------------------------------------------------------------------------------

@app.route('/settings')
def settings():
  return render_template('settings.html', title="Settings")

@app.route('/settings/practitioners')
def practitioners():
  practitioners = Practitioner.query.all()
  return render_template('practitioners.html', title="Practitioners", practitioners=practitioners)

@app.route('/settings/addpractitioner')
def addpractitioner():
  form = newPractitionerForm()
  if form.validate_on_submit():
    practitioner = Practitioner(firstName = form.firstName.data, lastName = form.lastName.data, 
                                practice = form.practice.data, claimNumber = form.claimNumber.data)
    db.session.add(practitioner)
    db.session.commit()
    flash('Practitioner sucessfully added!', 'success')
    return redirect( url_for('practitioners') )
  return render_template('addpractitioner.html', title="Add Practitioner", form=form)

@app.route('/settings/<int:practitioner_id>')
def practitioner(practitioner_id):
  practitioner = Practitioner.query_get_or_404(practitioner_id)
  return render_template('practitioner.html', title="Practitioner", practitioner=practitioner)

# ----------------------------------------------------------------------------------------------
# ********************************* Clinic Board & Posts ***************************************
# ----------------------------------------------------------------------------------------------
@app.route('/clinicboard')
def clinicboard():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=10)
  return render_template('clinicboard.html', title='ClinicBoard', posts=posts)

@app.route('/clinicboard/newpost', methods=['GET', 'POST'])
@login_required
def new_post():
  form = postForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, content=form.content.data, author=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Post created!', 'success')
    return redirect( url_for('clinicboard'))
  return render_template('createpost.html', title='New Post', form=form, legend='New Post')

@app.route('/clinicboard/<int:post_id>')
def post(post_id):
  post = Post.query.get_or_404(post_id)
  return render_template('post.html', title=post.title, post=post)

@app.route('/clinicboard/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def updatepost(post_id):
  post= Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)
  form = postForm()
  if form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    flash('Your post has been updated', 'success')
    return redirect( url_for('post', post_id=post.id))
  elif request.method == 'GET':
    form.title.data = post.title
    form.content.data = post.content
  return render_template('createpost.html', title='Update Post', form=form, legend='Update Post')

@app.route('/clinicboard/<int:post_id>/delete', methods=['POST'])
@login_required
def deletepost(post_id):
  post = Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash('Your post has been deleted', 'success')
  return redirect(url_for('clinicboard'))

@app.route('/user/<string:username>')
def user_posts(username):
  page = request.args.get('page', 1, type=int)
  user = User.query.filter_by(username=username).first_or_404()
  posts = Post.query.filter_by(author=user)\
    .order_by(Post.date_posted.desc())\
    .paginate(page=page, per_page=10)
  return render_template('userPosts.html', posts=posts, user=user)
# ----------------------------------------------------------------------------------------------
# ************************************** Patients **********************************************
# ----------------------------------------------------------------------------------------------
@app.route('/patients')
def patients():
  patients = Patient.query.all()
  return render_template('patients.html', title='Patients', patients=patients)

@app.route('/reports')
def reports():
  return render_template('reports.html', title='Reports')

@app.route('/tasks')
def tasks():
  return render_template('tasks.html', title='Tasks')

@app.route('/patients/addPatient', methods=['GET', 'POST'])
def addPatient():
  form = newPatientForm()
  if form.validate_on_submit():
    patient = Patient(pFirstName = form.pFirstName.data, pLastName= form.pLastName.data, pDOB=form.pDOB.data, 
      pIncidentDate=form.pIncidentDate.data, pClaimNumber=form.pClaimNumber.data, pScheduleID=form.pScheduleID.data)
    db.session.add(patient)
    db.session.commit()
    flash('Patient has been added.', 'success')
    return redirect( url_for('patients'))
  return render_template('addpatient.html', title='AddPatient', form=form)
