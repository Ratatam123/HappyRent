# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm

from wtforms import (StringField, IntegerField, BooleanField, TextAreaField,
                     PasswordField, SubmitField, SelectField)
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from property_project.db_models import User


class TypeForm(FlaskForm):
    item_type = SelectField('Category (click on the right to choose)', choices=[
        ('room', 'Room'), ('apartment', 'Apartment'), ('house', 'House')], validators=[DataRequired()])

    submit = SubmitField(
        'Save the category and let me give you more info about the offer')

class ItemForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = IntegerField('Number of rooms', validators=[DataRequired()])
    size = IntegerField('Size in square meters (whole number)', validators=[
                        DataRequired()], render_kw={"placeholder": "50"})
    rent = IntegerField('Rent in Euro (whole amount without cents)', validators=[
                        DataRequired()], render_kw={"placeholder": "100"})

    submit = SubmitField('Publish my offer!')


class LocalRegistrationForm(FlaskForm):

    password = PasswordField(
        'Add a local Password to your Github username', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add local password.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is not known to our system yet,'
                                  + ' please retry logging in via Github.')


class LocalLoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={"placeholder": "Put your Github username here."})
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

