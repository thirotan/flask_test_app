import os
from flask import Flask, render_template, request, url_for, redirect

from first_app import app, db
from first_app.models import Entry


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_entry():
    cmnt = request.form['comment']
    entry = Entry(
            comment = cmnt
            )
    db.session.add(entry)
    db.session.commit()
    return render_template('index.html')

@app.route('/entries')
def entry():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries.html', entries=entries)

