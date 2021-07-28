from django.contrib import admin
from django.utils.html import mark_safe
from boardapp.models import NoticeBoard, NoticeFile, EventBoard


class NoticeFileAdmin(admin.TabularInline):
    """NoticeFile Admin Definition"""

    model = NoticeFile


@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    """NoticeBoard Admin Definition"""

    icon_name = "book"

    inlines = (NoticeFileAdmin,)

    list_display = ("view_pk", "title", "view_author", "hit", "created")
    list_display_links = ("title",)
    fields = (
        "title",
        "author",
        "content",
        "created",
        "updated",
    )
    readonly_fields = (
        "created",
        "updated",
    )

    search_fields = ("title",)
    autocomplete_fields = ("author",)

    def view_pk(self, obj):
        return obj.pk

    view_pk.short_description = "번호"

    def view_author(self, obj):
        return obj.author.username

    view_author.short_description = "작성자"


@admin.register(EventBoard)
class EventBoardAdmin(admin.ModelAdmin):
    """EventBoard Admin Definition"""

    icon_name = "event"
    list_display = ("view_pk", "view_thumbnail", "title", "hit", "created", "updated")
    list_display_links = ("title",)

    fields = (
        "thumbnail",
        "title",
        "content",
        "event_start_date",
        "event_end_date",
        "hit",
        "created",
        "updated",
    )
    readonly_fields = (
        "created",
        "updated",
        "hit",
    )

    def view_pk(self, obj):
        return obj.pk

    view_pk.short_description = "번호"

    def view_thumbnail(self, obj):
        return mark_safe(
            f"<img src='{obj.thumbnail.url}' alt='{obj.title}' width='60px'/>"
        )

    view_thumbnail.short_description = "썸네일"
