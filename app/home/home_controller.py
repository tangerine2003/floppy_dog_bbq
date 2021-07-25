# from app import home
from flask import Blueprint, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


home = Blueprint("home", __name__, template_folder="./templates")


class Subscription(FlaskForm):
    email_sms = StringField("email_sms", validators=[DataRequired()])


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/about-us")
def about():
    return render_template("about-us.html")


@home.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")


@home.route("/gallery")
def gallery():
    return render_template("gallery.html")


@home.route("/subscribe")
def subscribe_to_alerts():
    form = Subscription()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("subscribe.html", form=form)


@home.route("/unsubscribe")
def unsubscribe_from_alerts():
    form = Subscription()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("unsubscribe.html", form=form)
