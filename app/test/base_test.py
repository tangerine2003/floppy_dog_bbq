from flask_testing import TestCase
from manage import app
import unittest


class TestBaseCase(TestCase):
    """Base Tests"""

    def create_app(self):
        app.config.from_object("webapp.main.config.TestingConfig")
        return app

    def test_app(self):
        self.assertTrue(True, True)


if __name__ == "__main__":
    unittest.main()
