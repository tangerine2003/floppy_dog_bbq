from base_test import BaseTestCase
from app.home.services import email
import unittest


class TestSMTP(BaseTestCase):
    def test_send_email(self):
        pass
        email.send_email(
            "John Doe", "info@example.com", "111-111-1111", "This is my test message"
        )


if __name__ == "__main__":
    unittest.main()
