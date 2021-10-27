"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 26/10/21
@name: test_user_api
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

Users = get_user_model()
CREATE_USER_URL = reverse('users:create')


def create_user(**params):
    return Users.objects.create(**params)


class PublicUserApiTest(TestCase):
    """
     Tests the user api
    """

    def setUp(self):
        self.client = APIClient()

    def test_create_new_user_success(self):
        """Crear a new User successful"""
        payload = {
            'email': 'user@example.com',
            'password': '123455qwerty',
            'password_confirmation': '123455qwerty',
            'name': 'User test 1',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)  # first validate status code 201
        user = Users.objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)  # Validate password not within res.data for obvious reasons

    def test_users_exists(self):
        """
        Tests validate if an users already exists
        """
        payload = {
            'email': 'user_2@example.com',
            'password': '12345513414512365',
            'name': 'User test 2',
        }
        user = create_user(**payload)  # create the user
        payload['password_confirmation'] = payload['password']
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """
        Test validate password's long. The password must be  more than five characters.
        """
        payload = {
            'email': 'user_3@example.com',
            'password': '123',
            'password_confirmation': '123',
            'name': 'User test 2',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user = Users.objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user)

    def test_password_confirmation(self):
        """
        Test for valid password and password_confirmation
        """
        payload = {
            'email': 'user_3@example.com',
            'password': 'qwerty12345',
            'password_confirmation': 'qwerty123456222222',
            'name': 'User test 2',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_name_is_required(self):
        """Check name validation in serializer """
        payload = {
            'email': 'test_user_23@example.com',
            'password': 'qwerty12345',
            'password_confirmation': 'qwerty12345'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', res.data.keys())
