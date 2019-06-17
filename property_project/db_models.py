from sqlalchemy import ForeignKey
import datetime

from property_project import app, db
from flask_dance.contrib.google import make_google_blueprint, google

from flask_login import UserMixin, current_user
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage


class User(db.Model, UserMixin):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    properties = db.relationship('PropertyItem', backref='author', lazy=True)

    # def __repr__(self):
    #     f"User('{self.username}'),'{self.email}')"

    @property   # ersetzt jsonify()?? in routes ggueber Restaurant-App-Vorbild?
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'type': self.type,
        }


# to relate OAuth-user-info to local User-table
class OAuth(OAuthConsumerMixin, db.Model):  # OAuthConsumerMixin adds extra
    # attributes: provider, token etc.
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'))
    user = db.relationship('User')


class PropertyType(db.Model):
    __tablename__ = 'property_type'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'type': self.type,
        }


class PropertyItem(db.Model):
    __tablename__ = 'property_item'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False,
                      default="Best place ever.")
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.utcnow)
    description = db.Column(db.String(250), default="A nice place.")
    rent = db.Column(db.Integer)  # (db.Numeric(6,2))
    rooms = db.Column(db.Integer, default=1)  # default=set_default_rooms
    size = db.Column(db.Integer)  # (db.Numeric(6,1))
    property_id = db.Column(db.Integer, ForeignKey('property_type.id'))
    property_type = db.relationship('PropertyType')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "PropertyItem('{self.title},{self.date_posted}')".format(self)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'property_type': self.property_type.type,
            'title': self.title,
            'date_posted': self.date_posted,
            'description': self.description,
            'rent': self.rent,
            'rooms': self.rooms,
            'size': self.size,
        }


# Google OAuth blueprint
google_blueprint = make_google_blueprint(scope=["https://www.googleapis.com/auth/userinfo.profile",
                                                "https://www.googleapis.com/auth/userinfo.email"])
app.register_blueprint(google_blueprint, url_prefix="/google_login")
google_blueprint.storage = SQLAlchemyStorage(OAuth, db.session, user=current_user,
                                             user_required=False)



