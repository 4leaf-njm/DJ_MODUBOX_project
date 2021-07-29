from django.forms import ModelForm
from userapp.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm) :
    class Meta :
        model = User
        fields = (
            "username",
            "name",
            "password1",
            "password2",
            "email",
        )