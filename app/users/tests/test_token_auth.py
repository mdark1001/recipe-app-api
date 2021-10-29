"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 28/10/21
@name: test_token_auth
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from .test_user_api import CREATE_USER_URL, Users

LOGIN_URL = reverse('users:login')
# TOKEN_URL = reverse('users:token')


class TokenAuthTest(TestCase):
    """Test for token and authorization requests """

    def setUp(self):
        self.client = APIClient()
        self.payload = {
            'email': 'a_validemail@example.com',
            'password': 'SuperPassword123'
        }
        payload = self.payload.copy()
        payload['name'] = 'New User'
        self.user = Users.objects.create_user(**payload)

    def test_login_success(self):
        """Test  successful login for an user registered previously"""
        res = self.client.post(LOGIN_URL, self.payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token',res.data)

    def test_failed_login_user_doesnt_exists(self):
        """Email unregister and return an error 404 does not exists """
        res = self.client.post(LOGIN_URL, {
            'email': 'un_register_user@example.com',
            'password': '123456qwerty'
         })
      
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_token_in_response_successful(self):
        """ Validate token in body response """
        res = self.client.post(LOGIN_URL, self.payload)
        token = res.data.get('token')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertNotEqual(token,'')
        