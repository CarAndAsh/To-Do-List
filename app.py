from flask import Flask, render_template, request
from flask_bootstrap.static import css, js, fonts
from flask_bootstrap import Bootstrap
from forms import TaskCerator, Task, TaskList, TLGroup

# TODO realize classes for task, list, group of lists and m.b. app
# TODO every list or group of lists create link on nav-block by '+'
# TODO list looks like name on page-name in representation-parameters-view of tasks
# TODO task looks like check-text-edit-delete-catch
# TODO m.b.realize steps in task looks like task
# work time: 4 h

app = Flask(__name__)
b_app = Bootstrap(app)

task_text = []


@app.route('/<username>')
@app.route('/', methods=['GET', 'POST'])
def main_page(username=None):
    global task_text
    if request.method == 'POST':
        req = request.form.get(key='task')
        if req == 'clr':
            task_text = []
        else:
            task_text.append(req)
    context = {'title': 'To-Do List',
               # 'taskcreator': TaskCerator(),
               # 'task': Task(),
               # 'tasklist': TaskList(),
               # 'tlgroup': TLGroup(),
               'task_text': task_text}
    return render_template('main.html', **context)


@app.route('/info')
def info_page():
    return render_template('info.html', title='Info')


if __name__ == '__main__':
    app.run(debug=True)
