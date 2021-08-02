from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    name = models.CharField("사용자명", max_length=12, null=True)
    mobile = models.CharField("핸드폰번호", max_length=12, null=True)
    # secretCode = models.CharField("인증번호", max_length=6, null=True)

    agreement1 = models.BooleanField("개인정보처리방침 동의", default=False)
    agreement2 = models.BooleanField("이용약관 동의", default=False)

    class Meta:
        verbose_name_plural = "회원 리스트"


# class AcceptRecord(models.Model):
#     """AcceptRecord Model Definition"""

#     aceept_date = models.DateField("접속일", auto_now_add=True)
#     aceept_date_time = models.DateTimeField("접속시간", auto_now_add=True)
#     user_ip = models.CharField("아이피", max_length=30, default="0.0.0.0")
#     user_platform = models.CharField("플렛폼", max_length=30, default="ANY")

#     class Meta:
#         verbose_name_plural = "접속 리스트"
#         unique_together = ("aceept_date", "user_ip")

#     def __str__(self):
#         return "Aceept Record Information"
