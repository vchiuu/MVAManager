from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class postForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
  content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "What's on your mind?"})
  submit = SubmitField('Post')
