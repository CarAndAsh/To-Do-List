import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# TODO ...
# work time: 1.5 h

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/info')
def info_page():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)
