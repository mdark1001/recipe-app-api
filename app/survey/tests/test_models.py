"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 01/11/21
@name: test_models
"""
from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from survey.models.survey import Survey, Question, Option


class SurveyModelTests(TestCase):
    """Test over survey's models  """

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='an_email@example.com',
            password='SuperPassword',
            name='An User',
        )

    def test_create_an_survey(self):
        """Create a survey successful and check it properties like name and created date """
        today = date.today()
        survey = Survey.objects.create(
            name='New Survey',
            owner=self.user,
        )
        self.assertFalse(survey)
        self.assertEqual(survey.name, 'New Survey')
        self.assertEqual(survey.created.today(), today)

    def test_create_survey_questions(self):
        """Create a survey and multiple questions """
        survey = Survey.objects.create(
            name='New Survey',
            owner=self.user,
        )
        questions = [
            {
                'name': 'Which color do you prefer?',
                'options': ['Red', 'Blue', 'Green', 'Purple', 'Yellow']
            },
            {
                'name': 'Which weather do you like?',
                'options': ['Warm', 'Cold', 'Hot', 'Cloudy']
            }
        ]
        for question in questions:
            # TODO - create question and them options :D

            for option in question['option']:
                pass
