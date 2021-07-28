from django.apps import AppConfig


class UserappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "userapp"
    verbose_name = "2 _ 회원 관리"
    icon_name = "account_circle"
