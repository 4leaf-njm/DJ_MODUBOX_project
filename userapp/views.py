from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from core.views import CustomCreateView, CustomUpdateView, CustomTemplateView
from userapp.forms import CustomUserCreationForm
from userapp.models import User
from django.urls import reverse, reverse_lazy
from userapp.decorators import account_ownwership_required
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core import mail
import string
import random

# settings.configure()

has_ownwership = [
    login_required,
    account_ownwership_required,
]


def get_secret_code():
    secret_code = ""

    for i in range(6):
        secret_code += random.choice(string.digits)
    return secret_code


def send_email(email, secret):
    print(secret)
    print(secret)
    print(secret)
    print(secret)
    to = [email]
    recipient_list = [email]
    print(to)
    print(to)
    print(to)
    print(to)
    from_email = "4leaf.ysh@gmail.com"
    email_from = "4leaf.ysh@gmail.com"
    subject = "π [λͺ¨λλ°μ€] μΈμ¦μ½λ λ©μΌμλλ€."
    # message = "μλλ λͺ¨λλ°μ€μμ λ³΄λΈ μΈμ¦μ½λ μλλ€. μΈμ¦μ½λλ₯Ό λ³΅μ¬ν΄μ μ¬μ΄νΈ μμ λΆμ¬λ£μ΄ μ£ΌμΈμ.<br />μΈμ¦μ½λ : <b>" + secret + "</b>"
    message = "μλλ λͺ¨λλ°μ€μμ λ³΄λΈ μΈμ¦μ½λ μλλ€. μΈμ¦μ½λλ₯Ό λ³΅μ¬ν΄μ μ¬μ΄νΈ μμ λΆμ¬λ£μ΄ μ£ΌμΈμ."
    # EmailMessage(
    #     # auth_user='4leaf.ysh@gmail.com',
    #     # auth_password='nvpdqofovkebects',
    #     subject=subject,
    #     message= message,
    #     from_email=from_email,
    #     to=to
    # )

    # send_mail('This is the title of the email',
    # 'This is the message you want to send',
    # settings.DEFAULT_FROM_EMAIL,
    # [
    #     settings.EMAIL_HOST_USER,
    #     '4leaf.njm@gmail.com' # add more emails to this list of you want to
    # ]

    # res = send_mail(
    #     subject = 'Subject here',
    #     message = 'Here is the message.',
    #     from_email = 'mail@gmail.com',
    #     recipient_list = ['4leaf.njm@gmail.com'],
    #     fail_silently=False,
    # )
    # print(res)
    # send_mail('μλνμΈμ.', 'μλνμΈμ!', '4leaf.njm@gmail.com', ['4leaf.njm@gmail.com'], fail_silently=False)
    # connection = mail.get_connection()   # κΈ°λ³Έ μ΄λ©μΌ μ°κ²° μ¬μ©
    # print(connection)
    # connection.open()
    # email = mail.EmailMessage(
    #     'Hello',
    #     'Body goes here',
    #     '4leaf.njm@gmail.com',
    #     ['4leaf.njm@gmail.com'],
    #     connection=connection,
    # )
    # email.send()
    # connection.close()


class UserCreateView(CustomCreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("userapp:login")
    template_name = "userapp/user_create.html"


@method_decorator(has_ownwership, "get")
@method_decorator(has_ownwership, "post")
class UserMypageView(CustomUpdateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:home")
    template_name = "userapp/mypage.html"


class UserFindView(CustomTemplateView):
    template_name = "userapp/find.html"

    def post(self, request, *args, **kwargs):
        find_type = self.request.POST.get("find_type")
        name = self.request.POST.get("name")
        username = self.request.POST.get("username")
        email = self.request.POST.get("email")

        if find_type == "1":
            users = User.objects.all().filter(name=name, email=email)

            if len(users) > 0:
                return render(
                    request,
                    "userapp/find_id_confirm.html",
                    {"id": users[0].username[:-3]},
                )
            else:
                return render(request, "userapp/find_id_confirm.html", {"id": ""})

        elif find_type == "2":
            users = User.objects.all().filter(username=username, email=email)
            if len(users) > 0:
                print(users[0])
                print(users[0])
                print(users[0])
                print(users[0])
                secret = get_secret_code()
                send_email(email, secret)
                users[0].secretCode = secret
                users[0].save()
                return render(request, "userapp/find_pw_certification.html")
            else:
                return render(request, "userapp/find_pw_none.html")


class UserFindIdConfirmView(CustomTemplateView):
    template_name = "userapp/find_id_confirm.html"


class UserFindPwNoneView(CustomTemplateView):
    template_name = "userapp/find_pw_none.html"


class UserFindPwCertificationView(CustomTemplateView):
    template_name = "userapp/find_pw_certification.html"


class UserFindPwChangeView(CustomTemplateView):
    template_name = "userapp/find_pw_change.html"
