"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 22/10/21
@name: test_admin.py
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AdminSiteTest(TestCase):

    def setUp(self):
        """   """
        self.cliente = Client()
        self.password = 'Admin2021'
        self.admin = User.objects.create_superuser(
            email='admin@example.com',
            password=self.password,
        )
        self.user = User.objects.create_user(
            email='user@example.com',
            password=self.password
        )

    def test_check_login(self):
        login = self.client.login(
            username=self.admin.email,
            password=self.password,
        )
        self.assertEqual(login, True)

    def test_users_listed(self):
        """Here we must to have a user list
        change de username by user email  """
        login = self.client.login(
            username=self.admin.email,
            password=self.password,
        )
        self.assertEqual(login, True)
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.admin.name)
