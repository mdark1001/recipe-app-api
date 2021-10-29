from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers.user import UserLoginSerializer, UserSignupSerializer, UserSerializer

User = get_user_model()


class UserSignupView(APIView):
    """ View for register new users using the UserSignupSerializer """

    def post(self, request, *args, **kwargs):
        sr = UserSignupSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        user = sr.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        srlogin = UserLoginSerializer(data=data)
        srlogin.is_valid(raise_exception=True)
        user,token = srlogin.save()
        data={
            'user': UserSerializer(user).data,
            'token':token
        }
        return Response(data,status=status.HTTP_200_OK)