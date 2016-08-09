# -*- coding:utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('first_app.config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import first_app.webapp
