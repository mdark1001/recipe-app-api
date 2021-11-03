"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 03/11/21
@name: urls
"""
from django.urls import path, include
from survey.views.survey import SurveyViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'survey', SurveyViewSets, 'survey')
app_name = 'survey'

urlpatterns = router.urls
