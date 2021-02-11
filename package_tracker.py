from flask import Flask, render_template, Blueprint, redirect
# import app.routes as routes
# import app.api_routes as api_routes
from app.config import Config
# from .models import db
from app.shipping_form import ShippingForm

bp = Blueprint("root", __name__, url_prefix="")

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def root():
    return render_template("root.html")


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    print("*****************22***************")
    if form.validate_on_submit():
        # form.populate_obj(order)
        print("***************25*****************")
        return redirect("/")
    return render_template('shipping_request.html', form=form)
