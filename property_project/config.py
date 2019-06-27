# -*- coding: utf-8 -*-
import os


class Config:
    # os.environ.get('SECRET_KEY')
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

    CACHE_TYPE = "null"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///properties.db'

    # GOOGLE OAUTH
    # os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_ID = '646163642970-koimt79vmr3355q1sldsd9e68hvvr336' +\
        '.apps.googleusercontent.com'
    # os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
    GOOGLE_OAUTH_CLIENT_SECRET = 'asUsmHtCv1TsfWa-gsJBJoOd'

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    OAUTHLIB_RELAX_TOKEN_SCOPE = True






