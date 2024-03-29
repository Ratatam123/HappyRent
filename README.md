# HappyRent

## Purpose of this project

This Web App was created as part of the Fullstack Web development course by Udacity. Users of the App 
are authorized via OAuth2 (Google as a provider) and can create, read, update and delete ("CRUD" functionality)
offers for their real estate after logging in. For now, the application only runs locally and is equipped 
with a sqlite database in the backend.

## Prerequisites
* Virtual Box 
* Vagrant
* Python 3 installation in Vagrant environment
* (Unix style) Shell

## Getting started

[comment]: <> (Verlinkung?)
* set up vagrant: 
&nbsp;&nbsp;&nbsp;&nbsp;[More information on how to set it up](https://medium.com/@JohnFoderaro/how-to-set-up-a-local-linux-environment-with-vagrant-163f0ba4da77)
* clone github repository into your local vagrant directory

### Starting Vagrant

* cd into the Vagrant directory on your local machine
* type following commands in the Shell to start up Vagrant

```console
vagrant up
vagrant ssh
cd /vagrant
```

## Running the Application
    
[comment]: <> (Python version?)

### Authentication

The application uses Google as an OAuth2 provider. Users consequently need to have a Google user 
account to log in and use the website. 

#### Security Keys

The OAuth system requires a *Client Id* and a *Client Secret*. For the moment they are hardcoded in
the *config.py* file. 

```python
GOOGLE_OAUTH_CLIENT_ID = ...
GOOGLE_OAUTH_CLIENT_SECRET = ...
```
They can also be found in the *.keys.txt* file as environment variables and could normally
be copied in one's *bash_profile*, but as Vagrant is used in this project it would need to be
included in the *Vagrantfile* with a different syntax instead 
([For more details on this issue](https://stackoverflow.com/questions/19648088/pass-environment-variables-to-vagrant-shell-provisioner)).

#### Start the Application

* install the modules listed in *requirements.txt*
* cd into the project directory
* run following command in the Shell

```console
python run.py
```

* access http://localhost:5000/ in the web browser of your choice

##### Explanation of the Login Process

When users run the application and enter http://localhost:5000/ 
in their web browser, they are initially redirected to the Google sign in page. 
After successfully logging in to their Google Account they are redirected to the home view 
of the actual web app. Behind the scenes the user logging in is stored with their Google username in the database. 
Being logged in enables a user to create, read, update and delete their own 
offers in the application.


#### Issues

The log out functionality sometimes doesn't work properly after a user is being logged in for a 
longer period of time. The issue is likely linked to problems in the communication with the Google
API. Suggestions for improvements in the code are welcome. Relevant functions in *routes.py*: 

```python
google_login()
google_logged_in(blueprint, token)
logout()
```

### "CRUD" (create, read, update, delete) functionality

Once logged in a user can create an offer by clicking *Create an Offer!* in the navigation bar on top
of the site. The button *My Offers* on the other hand enables the user logged in to read, update
and delete his own offers.

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

&nbsp;&nbsp;&nbsp;&nbsp;[Flask Youtube tutorial series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
&nbsp;&nbsp;&nbsp;&nbsp;[Github repository of tutorial](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)

Flask Dance module by David Goldbaum for OAuth2 in Flask:

&nbsp;&nbsp;&nbsp;&nbsp;[Documentation Flask Dance](https://flask-dance.readthedocs.io/en/latest/)
&nbsp;&nbsp;&nbsp;&nbsp;[Github Flask Dance](https://github.com/singingwolfboy/flask-dance)

&nbsp;&nbsp;&nbsp;&nbsp;[Tutorial for using Flask Dance](https://www.youtube.com/watch?v=MiHVTHzIgyE)

