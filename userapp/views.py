from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from core.views import CustomCreateView, CustomUpdateView, CustomTemplateView
from userapp.forms import CustomUserCreationForm
from userapp.models import User
from django.urls import reverse, reverse_lazy
from userapp.decorators import account_ownwership_required


has_ownwership = [
    login_required,
    account_ownwership_required,
]


class UserCreateView(CustomCreateView) :
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "userapp/user_create.html"
    
    
@method_decorator(has_ownwership, 'get')
@method_decorator(has_ownwership, 'post')
class UserMypageView(CustomUpdateView) :
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "userapp/mypage.html"


class UserFindView(CustomTemplateView) :
    template_name = "userapp/find.html"

class UserFindIdConfirmView(CustomTemplateView) :
    template_name = "userapp/find_id_confirm.html"

class UserFindPwCertificationView(CustomTemplateView) :
    template_name = "userapp/find_pw_certification.html"

class UserFindPwChangeView(CustomTemplateView) :
    template_name = "userapp/find_pw_change.html"


