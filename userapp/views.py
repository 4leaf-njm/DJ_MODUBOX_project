from django.shortcuts import render
from core.views import CustomCreateView
from userapp.forms import CustomUserCreationForm
from userapp.models import User
from django.urls import reverse, reverse_lazy


class UserCreateView(CustomCreateView) :
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "userapp/user_create.html"