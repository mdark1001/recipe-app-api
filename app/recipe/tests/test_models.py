"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 01/11/21
@name: test_models
"""

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class RecipeTestModels(TestCase):
    """Testing over  models    """
