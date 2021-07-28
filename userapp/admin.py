from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "name",
        "mobile",
        "is_staff",
    )

    fieldsets = (
        (
            "기본정보",
            {
                "fields": (
                    "username",
                    "name",
                    "email",
                    "mobile",
                ),
            },
        ),
        (
            "이용약관 동의",
            {
                "fields": (
                    "agreement1",
                    "agreement2",
                ),
            },
        ),
        (
            "가입/로그인 정보",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                ),
            },
        ),
    )


# @admin.register(AcceptRecord)
# class AcceptRecord(admin.ModelAdmin):
#     """AcceptRecord Admin Definition"""

#     def has_add_permission(self, request):
#         return False

#     icon_name = "assessment"
#     list_display = (
#         "user_ip",
#         "user_platform",
#         "aceept_date",
#         "aceept_date_time",
#     )
#     list_display_links = ("user_ip",)

#     list_filter = ("aceept_date",)
#     fields = (
#         "user_ip",
#         "user_platform",
#         "aceept_date",
#         "aceept_date_time",
#     )
#     readonly_fields = (
#         "user_ip",
#         "user_platform",
#         "aceept_date",
#         "aceept_date_time",
#     )
