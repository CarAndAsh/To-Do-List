from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired


class TaskCreator(FlaskForm):
    task_text = StringField('Введите текст задачи: ', validators=[InputRequired()])
    submit = SubmitField('add')


class Task(FlaskForm):
    check = BooleanField(label='')
    task_label = StringField(label='')


class TaskList(FlaskForm):
    pass


class TLGroup:
    pass


class LoginForm(FlaskForm):
    login = StringField()
    password = PasswordField()
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    login = StringField()
    new_password = PasswordField()
    repeat_password = PasswordField()
    submit = SubmitField('Зарегистрироваться')
