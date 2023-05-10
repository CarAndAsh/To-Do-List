from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, Label
from wtforms.validators import InputRequired


class TaskCreator(FlaskForm):
    task_text = StringField('Введите текст задачи: ', validators=[InputRequired()])
    submit = SubmitField('add')


class Task(FlaskForm):
    task_text = ''
    check = BooleanField(label=f'')
    task = StringField(render_kw={'placeholder': f'{task_text}',
                                  'state': 'disabled'})
    edit_btn = SubmitField('edit')
    del_btn = SubmitField('del')

    def add_task(self, task_text):
        self.task.render_kw['placeholder'] = task_text


class TaskList(FlaskForm):
    task_list = []

    # task_group = SelectMultipleField(choices=task_list, label='tasks')

    def add_task_to_list(self, task: Task):
        self.task_list.append(task)


class TLGroup:
    pass


class LoginForm(FlaskForm):
    login = StringField(label='Логин :', validators=[InputRequired()])
    password = PasswordField(label='Пароль :', validators=[InputRequired()])
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    login = StringField(label='Логин :', validators=[InputRequired()])
    new_password = PasswordField(label='Пароль :', validators=[InputRequired()])
    repeat_password = PasswordField(label='Повторите пароль :', validators=[InputRequired()])
    submit = SubmitField('Зарегистрироваться')
