from flask import render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import asc
from property_project import app, db
from property_project.forms import TypeForm, ItemForm
from property_project.db_models import User, PropertyItem, PropertyType


from property_project.db_models import google_blueprint, google
from flask_dance.consumer import oauth_authorized  # signal for Oauth
from sqlalchemy.orm.exc import NoResultFound

from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

import random
import string

login_manager = LoginManager(app)
login_manager.login_view = "google.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# @app.route("/")
# @app.route("/google/authorized")
@app.route("/home")
def home():
    if not google.authorized:
        return redirect(url_for("google.login"))

    property_types = []
    for type in db.session.query(PropertyType).distinct(PropertyType.type).group_by(PropertyType.type):
        property_types.append(type)

    return render_template('home.html', categories=property_types)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

#### GOOGLE LOGIN #####

@app.route("/")
@app.route('/google_login')
def google_login():
    if not google.authorized:  ## wiederhole authorized
        return redirect(url_for('google.login'))

    account_info = google.get("/oauth2/v1/userinfo")

    if account_info.ok:
        account_info_json = account_info.json()  # was passiert hier mit account_info??
        return redirect(url_for('home'))

    return '<h1>Try again!<h1>'


# signal communicating log-in status
@oauth_authorized.connect_via(google_blueprint)
def google_logged_in(blueprint, token):
    """
    The first argument is the object that should be called when the signal is emitted,
    the optional second argument specifies a sender."""

    account_info = blueprint.session.get("/oauth2/v1/userinfo")
    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['name']
        query = User.query.filter_by(username=username)

        try:
            # Test if user already exists in database
            user = query.one()
            print("no user found.")
        except NoResultFound:
            # Add the user to the database
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        login_user(user)
        flash("You are logged in with Google.", 'success')


@app.route("/logout")
def logout():

    try:
        token = app.blueprints["google"].token["access_token"]
        # revoking token on google side
        resp = google.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert resp.ok, resp.text
    except:
        logout_user()
        del google_blueprint.token
        return redirect(url_for('google.login'))

    logout_user()
    del google_blueprint.token
    return redirect(url_for('google.login'))


# JSON Endpoints

# all items
@app.route('/all_items/JSON')
def property_items_JSON():
    items = PropertyItem.query.all()
    return jsonify(all_items=[item.serialize for item in items])

# item by ID


@app.route('/property_item/<int:item_id>/JSON')
def item_by_id_JSON(item_id):
    item = PropertyItem.query.filter_by(id=item_id).one()
    return jsonify(PropertyItem=[item.serialize])

# items by type


@app.route('/<property_type>/items/JSON')
def items_by_type_JSON(property_type):

    items = PropertyItem.query.join(PropertyItem.property_type, aliased=True)\
        .filter_by(type=property_type)\
        .order_by(PropertyItem.date_posted.desc())

    return jsonify(items_by_type=[item.serialize for item in items])


# routes for each property type

@app.route("/houses")
def show_houses():

    page = request.args.get('page', 1, type=int)  # starting page

    houses = PropertyItem.query.join(PropertyItem.property_type, aliased=True)\
        .filter_by(type='house')\
        .order_by(PropertyItem.date_posted.desc())\
        .paginate(page=page, per_page=2)

    return render_template('houses.html', houses=houses)


@app.route("/apartments")
def show_apartments():

    page = request.args.get('page', 1, type=int)  # starting page
    apartments = PropertyItem.query.join(PropertyItem.property_type, aliased=True)\
        .filter_by(type='apartment')\
        .order_by(PropertyItem.date_posted.desc()).paginate(page=page, per_page=2)

    return render_template('apartments.html', apartments=apartments)


@app.route("/rooms")
def show_rooms():

    page = request.args.get('page', 1, type=int)  # starting page
    rooms = PropertyItem.query.join(PropertyItem.property_type, aliased=True)\
        .filter_by(type='room')\
        .order_by(PropertyItem.date_posted.desc()).paginate(page=page, per_page=2)

    return render_template('rooms.html', rooms=rooms)

# Creation of new item is distributed between 2 Forms, 1 used in each of the next 2 routes


@login_required
@app.route("/new_type", methods=['GET', 'POST'])
def new_type():
    if not google.authorized:
        return redirect(url_for('google.login'))
    type_form = TypeForm()
    if current_user.is_authenticated and type_form.validate_on_submit():
        item_type = PropertyType(type=type_form.item_type.data)
        db.session.add(item_type)
        db.session.commit()
        flash('Category "{}" has been saved, please add more details below.'.format(
            item_type.type.capitalize()), 'success')  # success => communicates with Bootstrap
        return redirect(url_for('new_item'))

    return render_template('create_type.html', title='New Item', form=type_form)


@login_required
@app.route("/new_item", methods=['GET', 'POST'])
def new_item():
    form = ItemForm()
    if current_user.is_authenticated and form.validate_on_submit():
        # get most recent type added to table PropertyType
        item_type = db.session.query(PropertyType).order_by(
            asc(PropertyType.date_posted)).first()

        item = PropertyItem(title=form.title.data,  property_type=item_type,
                            description=form.description.data, rooms=form.rooms.data,
                            size=form.size.data, rent=form.rent.data, author=current_user)

        db.session.add(item)
        db.session.commit()
        flash('Your offer has been created.', 'success')
        return redirect(url_for('home'))

    return render_template('create_item.html', title='New Item', form=form)


@app.route("/item/<int:item_id>")
def single_item(item_id):
    item = PropertyItem.query.get_or_404(item_id)
    return render_template('single_item.html', title=item.title, item=item)


@app.route("/item/<int:item_id>/update", methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    item = PropertyItem.query.get_or_404(item_id)
    if item.author != current_user:
        abort(403)
    form = ItemForm()
    if form.validate_on_submit():
        item.title = form.title.data
        item.description = form.description.data
        item.rooms = form.rooms.data
        item.size = form.size.data
        item.rent = form.rent.data

        db.session.commit()
        flash('Your offer has been updated!', 'success')
        return redirect(url_for('single_item', item_id=item.id))
    elif request.method == 'GET':
        form.title.data = item.title
        form.description.data = item.description
        form.rooms.data = item.rooms
        form.size.data = item.size
        form.rent.data = item.rent
    return render_template('create_item.html', title='Update item',
                           form=form, legend='Update item')


@app.route("/item/<int:item_id>/delete", methods=['POST'])
@login_required
def delete_item(item_id):
    item = PropertyItem.query.get_or_404(item_id)
    if item.author != current_user:
        abort(403)
    db.session.delete(item)
    db.session.commit()
    flash('Your item has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_items(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    prop_items = PropertyItem.query.filter_by(author=user)\
        .order_by(PropertyItem.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_items.html', prop_items=prop_items, user=user)


@app.route("/current_user/items")
def current_user_items():
    page = request.args.get('page', 1, type=int)  # for pagination
    user = User.query.filter_by(username=current_user.username).first_or_404()

    prop_items = PropertyItem.query.filter_by(author=user)\
        .order_by(PropertyItem.date_posted.desc())\
        .paginate(page=page, per_page=3)

    return render_template('current_user_items.html', prop_items=prop_items, user=user)



