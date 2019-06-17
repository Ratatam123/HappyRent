# turn module => package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_debugtoolbar import DebugToolbarExtension


import os
# for OAuth with Flask Dance module
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask(__name__)  # TypeError: 'NoneType' object is not subscriptable
app.debug = True


app.config['SECRET_KEY'] = '3516faa3660d50c1f5b34496db9e4819'

#toolbar = DebugToolbarExtension(app)
app.config["CACHE_TYPE"] = "null"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'

# GOOGLE OAUTH
app.config['GOOGLE_OAUTH_CLIENT_ID'] = '646163642970-koimt79vmr3355q1sldsd9e68hvvr336.apps.googleusercontent.com'
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = 'asUsmHtCv1TsfWa-gsJBJoOd'

app.config['OAUTHLIB_RELAX_TOKEN_SCOPE'] = True
db = SQLAlchemy(app)  # create engine etc. is created behind the scenes

from property_project import routes
from property_project import populate_db


# import blueprint instances from individual directories
# from property_project.users.routes import users
# from property_project.real_estate_items.routes import items
# from property_project.main.routes import main

# app.register_blueprint(users)
# app.register_blueprint(items)
# app.register_blueprint(main)

