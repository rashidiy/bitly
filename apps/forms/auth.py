from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import EmailField


class AuthSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username")
        field_classes = {
            "username": UsernameField,
            "email": EmailField,
        }