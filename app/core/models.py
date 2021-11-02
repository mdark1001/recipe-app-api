import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class UserManager(BaseUserManager):
    """
        Overwrite BaseUserManager for create custom user
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create a new user
        """
        if not email or not re.fullmatch(regex, email):
            raise ValueError('that email has not valid structure')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
            is_superuser=True,
            is_staff=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model that supports using email instead of username"""
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.name}"
