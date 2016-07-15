import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('first_app.config')

db = SQLAlchemy(app)

import first_app.webapp
