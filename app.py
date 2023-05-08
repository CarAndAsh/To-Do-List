from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import Task, TaskList, TLGroup, TaskCreator, LoginForm, RegistrationForm

# TODO realize classes for task, list, group of lists and m.b. app
# TODO every list or group of lists create link on nav-block by '+'
# TODO list looks like name on page-name in representation-parameters-view of tasks
# TODO task looks like check-text-edit-delete-catch
# TODO m.b.realize steps in task looks like task
# work time: 10 h

app = Flask(__name__)
b_app = Bootstrap(app)
app.config['SECRET_KEY'] = 'qwertyfasdqwerty!@#$654654'


# @app.route('/<username>')
@app.route('/', methods=['GET', 'POST'])
def main_page(username=None):
    task_text = ''
    context = {'title': 'To-Do List',
               'task': Task(),
               'task_creator': TaskCreator(),

               # 'tasklist': TaskList(),
               # 'tlgroup': TLGroup(),
               }
    if request.method == 'POST':
        req = request.get_data()
        print(req)

    return render_template('main.html', **context)


@app.route('/info')
def info_page():
    return render_template('info.html', title='Info')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    context = {'title': 'Login',
               'log_form': LoginForm()}
    return render_template('login.html', **context)


@app.route('/registraton', methods=['GET', 'POST'])
def reg_page():
    context = {'title': 'Registration',
               'reg_form': RegistrationForm()}
    return render_template('new_user_reg.html', **context)


@app.errorhandler(404)
def page_404(error):
    return render_template('page_404.html', title='Not found')


if __name__ == '__main__':
    app.run(debug=True)
