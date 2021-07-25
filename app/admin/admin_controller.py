from flask import Blueprint, render_template, url_for
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

# # from app import login_manager
from app.admin.login_forms import LoginForm

from app.admin.user_models import User

from app.admin.util import verify_pass

admin = Blueprint("admin", __name__, template_folder="./templates", url_prefix="/admin")


@admin.route("/")
def route_default():
    return redirect(url_for("admin.login"))


## Login & Registration


@admin.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    if "login" in request.form:

        # read form data
        username = request.form["username"]
        password = request.form["password"]

        # Locate user
        user = User.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for("base_blueprint.route_default"))

        # Something (user or pass) is not ok
        return render_template(
            "accounts/login.html", msg="Wrong user or password", form=login_form
        )

    if not current_user.is_authenticated:
        return render_template("accounts/login.html", form=login_form)
    return redirect(url_for("home_blueprint.index"))


@admin.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("base_blueprint.login"))


# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return render_template("page-403.html"), 403


@admin.errorhandler(403)
def access_forbidden(error):
    return render_template("page-403.html"), 403


@admin.errorhandler(404)
def not_found_error(error):
    return render_template("page-404.html"), 404


@admin.errorhandler(500)
def internal_error(error):
    return render_template("page-500.html"), 500
