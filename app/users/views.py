from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.user import UserSignupSerializer, UserSerializer

User = get_user_model()


class UserSignupView(APIView):
    """ View for register new users using the UserSignupSerializer """

    def post(self, request, *args, **kwargs):
        sr = UserSignupSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        user = sr.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
