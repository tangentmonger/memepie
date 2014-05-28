import os
from flask import Flask

myapp = Flask(__name__)

@myapp.route('/')
@myapp.route('/intro.htm')
def hello():
    return 'Hello World!'


