from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        email = 'test@gmail.com'
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superUser(self):
        user = get_user_model().objects.create_superuser(
            'michael@gmail.com',
            "passowrd"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
