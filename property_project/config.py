import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    CACHE_TYPE = "null"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///properties.db'

    # GOOGLE OAUTH
    GOOGLE_OAUTH_CLIENT_ID = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    OAUTHLIB_RELAX_TOKEN_SCOPE = True

