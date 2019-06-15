from property_project import app ## automatically imports from __init__.py

if __name__ == '__main__':
  app.secret_key = '3516faa3660d50c1f5b34496db9e4819'
  #app.debug = True
  app.run(host = '0.0.0.0', port = 5000) # ssl_context='adhoc'
