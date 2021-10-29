"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 27/10/21
@name: urls.py
"""
from django.urls import path
from .views import UserLoginView, UserSignupView

app_name = 'users'

urlpatterns = [
    path('create/', UserSignupView.as_view(), name='create'),
    path('login/',UserLoginView.as_view(), name='login'),
]
