# -*- coding: utf-8 -*-

import os
<<<<<<< HEAD
import sys
import json
||||||| merged common ancestors
=======
import json
>>>>>>> ef6fc9527b6c14733e40abaf2b53746848037db9

<<<<<<< HEAD
# os.path.join(sys.path[0], 'some file.txt')
with open(os.path.join(sys.path[0],'property_project/config.json')) as config_file:
        config = json.load(config_file)
||||||| merged common ancestors
=======
with open('/config.json') as config_file:
        config = json.load(config_file)
>>>>>>> ef6fc9527b6c14733e40abaf2b53746848037db9

class Config:
    # os.environ.get('SECRET_KEY')
    SECRET_KEY = config.get('SECRET_KEY')

    CACHE_TYPE = "null"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///properties.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://happy_renter:best_rents@localhost/happyrent_db'
    
    # GOOGLE OAUTH
    # os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_ID = config.get('GOOGLE_OAUTH_CLIENT_ID')
    # os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
    GOOGLE_OAUTH_CLIENT_SECRET = config.get('GOOGLE_OAUTH_CLIENT_SECRET')

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    OAUTHLIB_RELAX_TOKEN_SCOPE = True




