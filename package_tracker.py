from flask import Flask, render_template, Blueprint, redirect
from flask_migrate import Migrate
# import app.routes as routes
# import app.api_routes as api_routes
from app.config import Config
# from .models import db
from app.shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def root():
    return render_template("root.html")


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        # form.populate_obj(order)
        return redirect("/")
    return render_template('shipping_request.html', form=form)
