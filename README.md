# Property Project

## Purpose of this project

This Web App was created as part of the Fullstack Web development course by Udacity. Users of the App 
are authorized via OAuth2 (Google as a provider) and can create, read, update and delete ("CRUD" functionality)
offers for their real estate after logging in. For now, the Application only runs locally and is equipped 
with a sqlite database in the backend.

## Prerequisites
* Virtual Box 
* Vagrant
* Python 3 installation in vagrant environment
* (Unix style) Terminal/Bash

## Getting started

[comment]: <> (Verlinkung?)
* set up vagrant: 
&nbsp;&nbsp;&nbsp;&nbsp;[Here you can find more information on how to set it up](https://medium.com/@JohnFoderaro/how-to-set-up-a-local-linux-environment-with-vagrant-163f0ba4da77)
* clone github repository into your local vagrant directory

### Starting Vagrant

* cd into vagrant directory of your local machine
* type following commands in the terminal to start up vagrant

```console
vagrant up
vagrant ssh
```

### Running the application
    
[comment]: <> (Python version?)

* install the modules listed in requirements.txt
* cd into the project directory
* run following command in the Terminal

```console
python3 run.py
```

* access http://localhost:5000/ in the web browser of your choice

### Authentication

The application uses Google as an OAuth2 provider. Users consequently need to have a Google user 
account to log in and use the website. 

When users run the application and enter http://localhost:5000/ 
in their web browser, they are initially redirected to the Google sign in page. 
After successfully logging in to their Google Account they are redirected to the home view 
of the actual web app. Behind the scenes they are stored with their Google username in the database. 
Being logged in enables them to create, read, update and delete their own 
offers in the application.

####  Security & Keys

The OAuth system requires a Client Id and a Client Secret. They can be found in the .keys.txt file.
You should copy the contents in your local .bash_profile ([OSX users can find more info here]
(https://natelandau.com/my-mac-osx-bash_profile/)).

If you fail to access your bash_profile, you can instead in the *\_\_init\_\_.py* file add the following lines 

```python
app.config['GOOGLE_OAUTH_CLIENT_ID'] = ...
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = ...
```

right below the line

```python
app = Flask(__name__)
```

and replace *...* with the values from the *.keys.txt* file. If you do it this way, you also need to 
comment out/delete the following lines in the *config.py* file.

```python
GOOGLE_OAUTH_CLIENT_ID = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET') 
```

#### Issues

The log out functionality sometimes doesn't work properly after a user is being logged in for a 
longer period of time. The issue is likely linked to the expiration of the OAuth token on the Google 
side. Suggestions for improvements in the code are welcome. Relevant functions in *routes.py*: 

```python
google_login()
google_logged_in(blueprint, token)
logout()
```
are welcome.

### JSON API endpoints

All offers

* http://localhost:5000/all_items/JSON

Offer by ID

* http://localhost:5000/property_item/item_id/JSON
* values for variable *item_id* in the URL: 1, 2, 3 .. (as long as there are entries in the database)

Offer by type (house, apartment, room)

* http://localhost:5000/property_type/items/JSON
* values for variable *property_type* in the URL: house, apartment or room



## References

Flask Video Tutorials by Corey Schafer:

&nbsp;&nbsp;&nbsp;&nbsp;[Flask Tutorial series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

Flask Dance module by David Goldbaum for OAuth2 in Flask:

&nbsp;&nbsp;&nbsp;&nbsp;[Documentation Flask Dance](https://flask-dance.readthedocs.io/en/latest/)
&nbsp;&nbsp;&nbsp;&nbsp;[Github Flask Dance](https://github.com/singingwolfboy/flask-dance)

&nbsp;&nbsp;&nbsp;&nbsp;[Tutorial for using Flask Dance](https://www.youtube.com/watch?v=MiHVTHzIgyE)

