from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email 

# Extend FlaskForm
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required')])
    email = EmailField('Email', validators=[DataRequired(message='Email is required')])
    submit = SubmitField('Submit')