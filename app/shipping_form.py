from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SelectField, BooleanField, SubmitField)
from wtforms.validators import DataRequired
from map.map import map

v = [DataRequired()]


class ShippingForm(FlaskForm):
    name_sender = StringField("Sender name", v)
    name_recipient = StringField("Recipient name", v)
    origin = SelectField("Origin", v, choices=map)
    destination = SelectField("Destination", v, choices=map)
    express_shipping = BooleanField("Express shipping")
    submit = SubmitField("Submit")
