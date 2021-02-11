from flask import Flask, render_template, Blueprint
# import app.routes as routes
# import app.api_routes as api_routes
from .config import Config
from .models import db

bp = Blueprint("root", __name__, url_prefix="")

app = Flask(__name__)
app.config.from_object(Config)

@bp.route("/")
def root():
    return render_template("root.html")