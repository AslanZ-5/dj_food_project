from django.test import TestCase
import os
from django.contrib.auth.password_validation import validate_password


class TestSettings(TestCase):
    def test_is_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY,'abc123')

        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak Secret Key ------{e.messages}'
            self.fail(msg)
