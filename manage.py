import os
import logging

# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
# from webapp import blueprint
from app import create_app, db, migrate
from loguru import logger
import unittest


# http://127.0.0.1:5000/api/v1/documentation

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


class InterceptHandler(logging.Handler):
    def emit(self, record):
        """sets logger options

        Parameters:
            record-- logging record
        Returns:
            None--
        """
        logger_opt = logger.opt(depth=1, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


# app = create_app(os.getenv("FLASK_ENV") or "localdev")
app = create_app()

# more log configuration for rotation, retention, and level
logger.add(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "logs/events.log"),
    level="DEBUG",
    format="{time} {level} {message}",
    backtrace=True,
    rotation="5 MB",
    retention=9,
)

# add logger
app.logger.addHandler(InterceptHandler())
logging.basicConfig(handlers=[InterceptHandler()], level=20)

app.app_context().push()


@app.after_request
def after_request(response):
    """allows cookies for CORS
    Parameters:
        response-- flask response
    Returns:
        response-- flask response
    """
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response


@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()


# # creates app manager
# manager = Manager(app)

# # # sets migration operator
# # migrate = Migrate(app, db, compare_type=True)

# # # adds migration functionality
# # manager.add_command("db", MigrateCommand)


# @manager.command
# def run():
#     """Command line argument to run the app
#     Returns:
#         None--
#     """
#     app.run()


# @manager.command
# def test():
#     """runs the unit tests
#     Returns:
#         int-- 0 if tests are successful
#     """
#     tests = unittest.TestLoader().discover("webapp/test", pattern="*test.py")
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1


if __name__ == "__main__":
    app.run()
