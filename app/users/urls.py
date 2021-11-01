"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 27/10/21
@name: urls.py
"""
from django.urls import path
from .views import UserLoginView, UserSignupView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('sign/', UserSignupView.as_view(), name='create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', UserProfileView.as_view(), name='me')
]
