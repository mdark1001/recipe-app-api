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
        self.assertIsNotNone(survey)
        self.assertEqual(survey.name, 'New Survey')
        self.assertEqual(survey.created.date(), today)

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
            q = Question(name=question['name'], survey=survey)
            q.save()
            for option in question['options']:
                o = Option(
                    question=q,
                    name=option,
                )
                o.save()
        self.assertEqual(len(questions), survey.total_questions)
        # print(survey.questions.all())
        self.assertEqual(questions[0]['name'], survey.questions.all()[0].name)

    def test_get_only_surveys_actives(self):
        """Test over custom manager by get surveys active"""
        surveys = [
            {'name': 'New survey', 'owner': self.user, 'is_active': True},
            {'name': 'New survey 2', 'owner': self.user, 'is_active': False}
        ]
        count_surveys_actives_array = len(list(filter(lambda s: s['is_active'], surveys)))
        for s in surveys:
            Survey.objects.create(**s)
        count_surveys_actives = Survey.actives.count()
        self.assertEqual(count_surveys_actives_array, count_surveys_actives)
    # def test_
