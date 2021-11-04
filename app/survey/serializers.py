"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 03/11/21
@name: serializers
"""
from abc import ABC

from rest_framework import serializers

from survey.models.survey import Survey, Question, Option


class OptionModelSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Option
        fields = ['name',]


class QuestionsSerializer(serializers.ModelSerializer):
    options = OptionModelSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['name', 'options']


class SurveyModelSerializer(serializers.ModelSerializer):
    """Model Serializer for Survey model  """
    questions = QuestionsSerializer(many=True, read_only=True, required=False)
    slug = serializers.SlugField(required=False, )


    class Meta:
        model = Survey
        fields = ['name', 'slug', 'is_active', 'owner', 'questions']

        # read_only_fields = ('questions',)
