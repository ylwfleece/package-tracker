from flask import Flask, render_template, Blueprint, redirect
from flask_migrate import Migrate
from app.config import Config
from app.models import db, Package 
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
        data = form.data
        new_package = Package(name=data["name_sender"], recipient=data["name_recipient"], origin=data["origin"], destination=data["destination"], location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        return redirect("/")
    return render_template('shipping_request.html', form=form)
