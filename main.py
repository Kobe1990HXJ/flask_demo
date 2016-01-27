#-*-coding:utf-8 -*-
#import sys
#sys.path.append('/cygdrive/c/Python27/Lib/site-packages')

import flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
app = flask.Flask(__name__)
bootstrap = Bootstrap(app)

fruits_list = ["apple", "orange", "banana"]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/fruits')
def fruits():
    return render_template('fruits.html',fruits=fruits_list)

if __name__ == '__main__':
    app.run(debug=True)
