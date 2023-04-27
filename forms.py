import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TaskCerator(FlaskForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        entry = StringField("Введите текст задачи...")
        btn = SubmitField('+')


class Task(FlaskForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


task_list = {name: Task for name in ('сделать', 'прочесть', 'написать', 'отправить')}


class TaskList(FlaskForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TLGroup:
    def __init__(self):
        pass
