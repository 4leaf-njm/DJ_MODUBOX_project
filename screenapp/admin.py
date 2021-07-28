from django.contrib import admin
from screenapp.models import MainBanner
from django.utils.html import mark_safe


@admin.register(MainBanner)
class MainBannerAdmin(admin.ModelAdmin):
    """MainBanner Admin Definitions"""

    icon_name = "image"
    list_display = (
        "get_image",
        "title",
        "updated",
        "sort",
    )
    list_display_links = ("title",)
    ordering = ["sort"]

    fields = (
        "image_file",
        "mobile_image_file",
        "title",
        "content",
        "sort",
        "updated",
    )
    readonly_fields = ("updated",)

    def get_image(self, obj):
        return mark_safe(
            f"<img style='margin-left : 15px' src={obj.image_file.url} alt={obj.title} with='200px' height='50px' />"
        )

    get_image.short_description = "베너 이미지"
