from flask import render_template, request, url_for, redirect

from . import app, db
from first_app.models import Entry


@app.route('/')
def index():
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

