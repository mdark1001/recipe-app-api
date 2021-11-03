"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 03/11/21
@name: test_ennpoint_survey
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from survey.models.survey import Survey

User = get_user_model().objects
SURVEY_URL = reverse('survey:survey-list')
LIST_SURVEY_URL = reverse('survey:survey-list')


class SurveyEndpointTests(TestCase):
    """Test over API survey endpoint  """

    def setUp(self):
        """Initialize test"""
        self.client = APIClient()
        self.user = User.create_user(
            email='test@email.com',
            password='123456122',
            name='New User'
        )

        self.user_two = User.create_user(
            email='test2@email.com',
            password='12345612211',
            name='New User'
        )

    def test_create_successful_survey(self):
        """Create a survey using the api endpoint """
        self.client.force_authenticate(self.user)
        res = self.client.post(SURVEY_URL,
                               {
                                   'name': 'When is your birth day?',
                                   'owner': self.user.pk,
                               })
        print(res.content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_fail_create_survey_unauthorized(self):
        """Validate if  request has a user authorized to create surveys"""
        res = self.client.post(SURVEY_URL, {"name": "When is your birth day?"})
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_my_own_surveys(self):
        """ list my own surveys"""
        surveys = [
            {'name': 'New survey 1', 'owner': self.user, 'is_active': True},
            {'name': 'New survey 2', 'owner': self.user, 'is_active': False},
            {'name': 'New survey 3', 'owner': self.user, 'is_active': False},
            {'name': 'New survey 4', 'owner': self.user, 'is_active': True},
            {'name': 'New survey 5', 'owner': self.user, 'is_active': False},
            {'name': 'New survey 6', 'owner': self.user_two, 'is_active': False},
            {'name': 'New survey 7', 'owner': self.user_two, 'is_active': True},
        ]
        for survey in surveys:
            Survey.objects.create(**survey)
        self.client.force_authenticate(user=self.user)
        res = self.client.get(LIST_SURVEY_URL)
        user_total_surveys = len(list(filter(lambda s: s['owner'] == self.user, surveys)))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
      #  self.assertIn('surveys', res.data)
        self.assertEqual(user_total_surveys, len(res.data))
