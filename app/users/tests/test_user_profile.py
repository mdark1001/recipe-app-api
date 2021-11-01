"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 30/10/21
@name: test_user_profile
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

LOGIN_URL = reverse('users:login')
USER_PROFILE = reverse('users:me')


class UserProfileTests(TestCase):
    """Validate if an user can check your profile and update this,
        Try if an user can't update another profile.
    """

    def setUp(self):
        self.client = APIClient()
        self.user_one = User.objects.create_user(
            **{
                'name': 'User one',
                'password': 'qwerty12345',
                'email': 'userone@example.com',
            }
        )
        self.user_two = User.objects.create_user(
            **{
                'name': 'User two',
                'password': 'qwerty12345',
                'email': 'usertwo@example.com',
            }
        )

    def test_valid_permissions(self):
        """Check if you are logged """

        res = self.client.get(USER_PROFILE)
        self.assertTrue(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_check_your_profile(self):
        """Check if an user cna check your profile and get information """
        res = self.client.post(LOGIN_URL, {'password': 'qwerty12345', 'email': 'userone@example.com'})
        # print(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=self.user_one)
        res = self.client.get(USER_PROFILE)
        # print(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_profile_post_method_isnt_allowed(self):
        """In user profile post method is not allowed """
        self.client.force_authenticate(user=self.user_one)
        res = self.client.post(USER_PROFILE, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_profile_user(self):
        """Update the profile user using endpoint and method path """
        payload = {
            'name': 'New Name'
        }
        self.client.force_authenticate(user=self.user_one)
        res = self.client.patch(USER_PROFILE, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.user_one.refresh_from_db()
        self.assertEqual(self.user_one.name, payload['name'])
