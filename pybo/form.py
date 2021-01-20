from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수지렁')])
    content = TextAreaField('내용', validators=[DataRequired('내요용은 필수지렁')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수지렁22')])


class UserForm(FlaskForm):
    username = StringField('uuuusername', validators=[DataRequired('한글1'), Length(min=3, max=25)])
    password1 = PasswordField('pppasword', validators=[DataRequired('한글2')])
    password2 = PasswordField('pppasword ccconfirm', validators=[DataRequired('한글2'), EqualTo('password1', 'not match pw')])
    email = EmailField('eeemail', validators=[DataRequired('한글4'), Email('이멜?')])


class UserLoginForm(FlaskForm):
    username = StringField('uuser nname', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('ppassword', validators=[DataRequired()])
