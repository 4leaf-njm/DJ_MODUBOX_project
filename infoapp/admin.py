from django.contrib import admin
from infoapp.models import FooterInfo, LogoInfo, AgreementInfo


@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    """FooterInfo Admin Definition"""

    icon_name = "info"
    list_display = (
        "title",
        "content",
        "sort",
        "updated",
    )
    list_display_links = ("title",)
    fields = (
        "title",
        "content",
        "sort",
        "updated",
    )
    ordering = ["sort",]

    readonly_fields = ("updated",)


@admin.register(LogoInfo)
class LogoInfoAdmin(admin.ModelAdmin):
    """LogoInfo Admin Definition"""

    icon_name = "info"

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = (
        "title",
        "updated",
    )
    list_display_links = ("title",)
    fields = (
        "title",
        "logo_file",
        "updated",
    )

    readonly_fields = ("updated",)


@admin.register(AgreementInfo)
class LogoInfoAdmin(admin.ModelAdmin):
    """AgreementInfo Admin Definition"""

    icon_name = "info"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = (
        "title",
        "content",
    )
    list_display_links = ("title",)
    fields = (
        "title",
        "content",
        "updated",
    )

    readonly_fields = ("updated",)
