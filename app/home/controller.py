from app import home
from flask import Blueprint, render_template


home = Blueprint("home", __name__)


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/about-us")
def about():
    return render_template("about-us.html")


@home.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")
