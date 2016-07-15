import os
from flask import Flask, render_template, request

from first_app import app


@app.route('/')
def hello_world():
    return render_template('index.html', name='First App')

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    return 'Hello' + name + '!'

