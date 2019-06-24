# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from property_project.config import Config
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(Config)  # load OAUTH keys etc. into the app
app.debug = True

#toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)  # create engine etc. is created behind the scenes

from property_project import routes
from property_project import populate_db


