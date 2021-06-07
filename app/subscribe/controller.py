from werkzeug.utils import redirect
from app import subscribe
from flask import Blueprint, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

subscribe = Blueprint("subscriptions", __name__, template_folder="./templates")


class Subscription(FlaskForm):
    email_sms = StringField("email_sms", validators=[DataRequired()])


@subscribe.route("/subscribe")
def subscribe_to_alerts():
    form = Subscription()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("subscribe.html", form=form)


@subscribe.route("/unsubscribe")
def unsubscribe_from_alerts():
    form = Subscription()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("unsubscribe.html", form=form)
