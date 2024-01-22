from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.fields.html5 import EmailField

from model import Register


class FormRegister(FlaskForm):
    name = StringField('Username',validators=[
        validators.DataRequired(), 
        validators.Length(1, 10)])
    email = EmailField('Email', validators=[
        validators.DataRequired(), 
        validators.Email()])
    password = PasswordField('Password', validators=[
        validators.DataRequired(), 
        validators.Length(8, 20), 
        # 'password2' 用來確認兩次密碼是否相同
        validators.EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confirm Password', validators=[
        validators.DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Register.query.filter_by(email=field.data).first():
            raise validators.ValidationError('Email already registered.')
        
    def validate_name(self, field):
        if Register.query.filter_by(name=field.data).first():
            raise validators.ValidationError('Username already used.')
        