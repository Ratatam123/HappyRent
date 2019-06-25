# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from property_project.config import Config

app = Flask(__name__)
app.config.from_object(Config)  # load OAUTH keys etc. into the app

db = SQLAlchemy(app)  # create engine etc. is created behind the scenes

from property_project import routes
from property_project import populate_db


