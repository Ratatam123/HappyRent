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
* type following commands in the terminnal to start up vagrant

```console
vagrant up
vagrant ssh
```

### Running the application
    
[comment]: <> (Python version?)

* install the modules listed in requirements.txt
* cd into the property_project directory
* run following command in the Terminal

```console
python3 run.py
```

### Authentication

When users run the application and enter http://localhost:5000/ in their Browser they are redirected
to the the Google sign in, which acts as an OAuth2 provider. After successfully logging in to their 
Google Account they are redirected to the home view of the actual web app. Behind the scenes they
are saved as users in the database under their Google username. Being logged in enables them to create,
read, update and delete their own offers in the application.

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

