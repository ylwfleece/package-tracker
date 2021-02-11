from flask import Flask, render_template, Blueprint
# import app.routes as routes
# import app.api_routes as api_routes
from app.config import Config
# from .models import db

bp = Blueprint("root", __name__, url_prefix="")

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def root():
    return render_template("root.html")


@app.route("/new_package")
def new_package():
    return render_template('shipping_request.html')

