## turn module => package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt  ## User-Login C. Schafer
from flask_login import LoginManager ## Login-Extension ## User-Login C. Schafer
#from flask_dance.contrib.github import make_github_blueprint, github

from flask_debugtoolbar import DebugToolbarExtension
#from property_project.db_models import User
## vgl. Flask-Dance Tutorial
# from flask_login import UserMixin, current_user  ## UserMixin adds properties to self created User class (in db_models)

# from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage

## original
# from flask_dance.consumer.backend.sqla import SQLAlchemyBackend

import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # for OAuth with Flask Dance module


app = Flask(__name__)## TypeError: 'NoneType' object is not subscriptable
app.debug = True

## Positioning new => after blueprint usage
# login_manager = LoginManager(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

### notwendig?!
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'

app.config['SECRET_KEY'] = '3516faa3660d50c1f5b34496db9e4819' ## terminal; import secrets; secrets.token_hex(16)

#toolbar = DebugToolbarExtension(app)
app.config["CACHE_TYPE"] = "null"


# wo eingesetzt??
# folgende beide Zeilen bei Schafer vs. Udacity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
## erwartet, dass sie existiert!

### alternativ zu: dem make_github_blueprint() Konstruktor mitgeben!
app.config['GITHUB_OAUTH_CLIENT_ID'] ='65897babe75c29f9eadf'
app.config['GITHUB_OAUTH_CLIENT_SECRET'] = '3bbeaa11e9a8800ab6ae9b0ff7e044b321ab4233'

### GOOGLE OAUTH
app.config['GOOGLE_OAUTH_CLIENT_ID'] ='646163642970-koimt79vmr3355q1sldsd9e68hvvr336.apps.googleusercontent.com'
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = 'asUsmHtCv1TsfWa-gsJBJoOd'

app.config['OAUTHLIB_RELAX_TOKEN_SCOPE'] = True 
db = SQLAlchemy(app) ## create engine etc. is created behind the scenes



from property_project import routes

## import blueprint instances from individual directories
# from property_project.users.routes import users
# from property_project.real_estate_items.routes import items
# from property_project.main.routes import main

# app.register_blueprint(users)
# app.register_blueprint(items)
# app.register_blueprint(main)

from property_project import populate_db

## Login von C. Schaefer

    # bcrypt = Bcrypt(app) ## User-Login (durch Google OAuth ersetzbar?!)
    # login_manager = LoginManager()#LoginManager(app)
    # login_manager.init_app(app)


