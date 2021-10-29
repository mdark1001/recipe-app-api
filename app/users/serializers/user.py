"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 26/10/21
@name: user
"""
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import password_validation
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user objects  """

    class Meta:
        model = get_user_model()  # Here return user model class
        fields = [
            'name',
            'email',
        ]
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }

    def create(self, validated_data):
        """ Create a new user with  encrypted password and return it
            :param validated_data
        """
        return User.objects.create_user(**validated_data)


class UserSignupSerializer(serializers.Serializer):
    """Serializer can validated password confirmation """
    name = serializers.CharField(
        min_length=2,
        max_length=255
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        error_messages={
            'unique': 'That email already exists, please try with other.'
        }
    )
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )
    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self, data):
        """Custom validation for """
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Password and password confirmation field are required ')
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(data['password'])
        return data

    def create(self, validated_data):
        """

        """
        validated_data.pop('password_confirmation')
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    """User serializer for login.
    Check email and password and return a new token"""

    email = serializers.EmailField(
        min_length=2,
    )
    password = serializers.CharField(
        min_length=8,
        max_length=64,
        style=["input_type",'password'],
    )

    def validate(self, data):
        """Check  email and password using the authenticate django's function"""
        user = authenticate(
            username=data['email'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError(detail="""Email or password incorrect,
            " please check and try again""")
        # here we can add more validations around the user, 
        # e.g. Check if user has active, this acount is verified too.
        self.context['user'] = user
        return data 

    def create(self,validated_data):
        """After check credentials we must create a new token by the user"""

        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key