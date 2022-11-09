from django.test import TestCase
from django.contrib.auth.models import User


class Admin_check(TestCase):
    def setUp(self):
        self.test_super_user = User.objects.create_superuser(
            username="maddy", password="123"
        )

    def test_super_user(self):
        self.assertEqual((self.test_super_user.username), "maddy")
