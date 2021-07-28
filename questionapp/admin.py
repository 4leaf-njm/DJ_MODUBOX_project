from django.contrib import admin
from questionapp.models import QnaBoard, DirectQuestion, OrderBoard


@admin.register(OrderBoard)
class OrderBoardAdmin(admin.ModelAdmin):
    """OrderBoard Admin Definition"""

    def has_add_permission(self, request):
        return False

    icon_name = "filter_frames"

    list_display = (
        "view_pk",
        "title",
        "company",
        "name",
        "tel",
        "created",
        "is_completed",
    )
    list_display_links = ("title",)
    list_filter = (
        "created",
        "company",
    )

    ordering = ["-created"]

    fields = (
        "title",
        "company",
        "name",
        "password",
        "tel",
        "email",
        "pro_type",
        "pro_qny",
        "size_width",
        "size_length",
        "size_height",
        "design_yn",
        "paper_type",
        "print_spec",
        "coating",
        "processing",
        "content",
        "file_1",
        "file_2",
        "file_3",
        "created",
        "updated",
        "is_completed",
    )

    readonly_fields = (
        "title",
        "company",
        "name",
        "password",
        "tel",
        "email",
        "pro_type",
        "pro_qny",
        "size_width",
        "size_length",
        "size_height",
        "design_yn",
        "paper_type",
        "print_spec",
        "coating",
        "processing",
        "content",
        "file_1",
        "file_2",
        "file_3",
        "created",
        "updated",
    )

    def view_pk(self, obj):
        return obj.pk

    view_pk.short_description = "번호"


@admin.register(QnaBoard)
class QnaBoardAdmin(admin.ModelAdmin):
    """QnaBoard Admin Definition"""

    icon_name = "question_answer"
    list_display = ("view_pk", "title", "type", "created")
    list_display_links = ("title",)

    list_filter = ("type",)

    def view_pk(self, obj):
        return obj.pk

    view_pk.short_description = "번호"


@admin.register(DirectQuestion)
class DirectQuestionAdmin(admin.ModelAdmin):
    """DirectQuestion Admin Definition"""

    def has_add_permission(self, request):
        return False

    icon_name = "question_answer"

    list_display = ("view_pk", "title", "is_complete", "created", "updated")
    list_display_links = ("title",)
    list_filter = (
        "is_complete",
        "created",
    )

    fields = (
        "title",
        "content",
        "is_complete",
        "author",
        "answer",
        "answer_file",
        "created",
        "updated",
    )

    readonly_fields = (
        "title",
        "content",
        "author",
        "created",
        "updated",
    )

    def view_pk(self, obj):
        return obj.pk

    view_pk.short_description = "번호"
