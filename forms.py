from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, Label
from wtforms.validators import InputRequired
from itertools import count


class TaskCreator(FlaskForm):
    task_text = StringField('Введите текст задачи: ', validators=[InputRequired()])
    submit = SubmitField('add')


class Task(FlaskForm):
    task_text = ''
    check = BooleanField(label='')
    task_label = Label(field_id=f'{count}', text=f'{task_text}')

    def add_task(self, task_text):
        self.task_label.text = task_text
        print(self.task_label.text, self.task_label.field_id)


class TaskList(FlaskForm):
    task_list = []

    # task_group = SelectMultipleField(choices=task_list, label='tasks')

    def add_task_to_list(self, task: Task):
        self.task_list.append(task)


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
