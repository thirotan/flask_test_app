import os
from flask import Flask, render_template, request

from first_app import app, db
from first_app.models import Entry


@app.route('/')
def hello_world():
    return render_template('index.html', name='First App')

@app.route('/add', methods=['POST'])
def add_entry():
    cmnt = request.form['comment']
    entry = Entry(
            comment = cmnt
            )
    db.session.add(entry)
    db.session.commit()
    return 'Hello' + cmnt + '!'

