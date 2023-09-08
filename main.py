# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Welkom at the farm! this is my latest test! '

@app.route('/cow')
def cow():
    return 'MOoooOo!'


@app.route('/rooster')
def rooster():
    return 'Kukeleeekuuu!'

@app.route('/mice')
def mice():
    return  'Cheese!'
