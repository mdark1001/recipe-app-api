"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 03/11/21
@name: serializers
"""
from rest_framework import serializers

from survey.models.survey import Survey


class SurveyModelSerializer(serializers.ModelSerializer):
    """Model Serializer for Survey model  """

    class Meta:
        model = Survey
        fields = ['name', 'is_active', 'owner']

        # read_only_fields = ('owner', 'created',)
