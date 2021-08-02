from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from userapp.views import UserCreateView, UserMypageView, UserFindView, UserFindIdConfirmView, UserFindPwCertificationView, UserFindPwChangeView

app_name = "userapp"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="userapp/login.html"), name="login"),
    path("join/", UserCreateView.as_view(), name="join"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("mypage/<int:pk>", UserMypageView.as_view(), name="mypage"),
    path("find/", UserFindView.as_view(), name="find"),
    path("find_id_confirm", UserFindIdConfirmView.as_view(), name="find_id_confirm"),
    path("find_pw_certification/", UserFindPwCertificationView.as_view(), name="find_pw_certification"),
    path("find_pw_change/", UserFindPwChangeView.as_view(), name="find_pw_change"),
]
