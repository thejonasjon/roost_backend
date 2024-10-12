from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersManagersTests(TestCase):

    def test_create_user(self):
        user = get_user_model()

        user.create_user(email="testemail@gmail.com", password="testP@ssw0rd")
        self.assertEqual(user.email, "testemail@gmail.com")
        self.assertFalse(user.is_staff, False)
        self.assertFalse(user.is_superuser, False)
        self.assertFalse(user.is_active, False)
        self.assertFalse(user.is_verified, False)
        self.assertFalse(user.is_active, False)

    def test_create_superuser(self):
        user = self.create_superuser(eamil="testsuperuser@gmail.com", password="testP@ssw0rd")
        self.assertEqual(user.email, "testsuperuser@gmail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_verified)
        self.assertTrue(user.is_active)