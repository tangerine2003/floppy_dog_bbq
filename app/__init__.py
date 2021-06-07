from flask import Flask
from .subscribe.controller import subscribe
from .home.controller import home

""" from .admin.routes import admin
from .api.routes import api
from .website.routes import website
from extensions import *
 """

from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

# from .config import config_by_name
# from webapp.main.util.jwt_extension import jwt
from flask_migrate import Migrate


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
ma = Marshmallow()
flask_bcrypt = Bcrypt()
migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config.from_object("config.DevConfig")
    # Initialise extensions
    db.init_app(app)
    ma.init_app(app)
    flask_bcrypt.init_app(app)
    migrate.init_app(app)

    with app.app_context():
        app.register_blueprint(subscribe, url_prefix="/subscriptions")
        app.register_blueprint(home)
        # app.register_blueprint(api, url_prefix="/api")
    return app
