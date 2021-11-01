from rest_framework import status, authentication, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

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
        user, token = srlogin.save()
        data = {
            'user': UserSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    """user profile view for update and retrieve their perfil"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = UserSerializer(
            user,
            data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserSerializer(user).data
        return Response(data)

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
