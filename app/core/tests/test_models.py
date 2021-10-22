"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 21/10/21
@name: test_models.py
"""
from django.test import TestCase
# it isn't recommended import directly user model,
# we can use a get_user_model for this propose
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ We must registered a new user with no existing email """
        email = 'email@mdark.com'
        password = 'SuperTestCurrent'

        user = User.objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """We must to normalized every time user's email,
         because user can introduce majuscule """
        email = 'user@UndefinedDomain.com'
        user = User.objects.create_user(
            email=email,
        )
        self.assertEqual(email.lower(), user.email)

    def test_new_user_with_not_valid_email(self):
        """Raise error for not valid emails  """
        with self.assertRaises(ValueError):
            User.objects.create_user('an invalid email')

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email='su@damin.com',
            password='SuperPassword'
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
