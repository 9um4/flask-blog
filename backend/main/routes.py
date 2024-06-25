from flask import render_template
from . import main

@main.route('/')
def home():
    return render_template('pages/index.html')

@main.route('/about')
def about():
    return render_template('pages/about.html')
