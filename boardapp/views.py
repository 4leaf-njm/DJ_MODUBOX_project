from django.shortcuts import render
from django.shortcuts import get_object_or_404
from boardapp.models import NoticeBoard
from core.views import CustomListView, CustomDetailView


class NoticeBoardListView(CustomListView):
    model = NoticeBoard
    context_object_name = "notice_list"
    template_name = "boardapp/notice_list.html"
    paginate_by = 20
    ordering = ["-created"]

    def get_queryset(self, *args, **kwargs):
        user_search_value = self.request.GET.get("search")

        if not user_search_value:
            return super().get_queryset()
        else:
            search_result_notice_list = NoticeBoard.objects.filter(
                title__startswith=user_search_value
            )
            return search_result_notice_list


class NoticeBoardDetailView(CustomDetailView):

    model = NoticeBoard
    context_object_name = "target_notice"
    template_name = "boardapp/notice_detail.html"

    def get(self, *args, **kwargs):

        current_notice_pk = kwargs["pk"]
        current_notice_object = get_object_or_404(NoticeBoard, pk=current_notice_pk)

        current_notice_object.hit += 1
        current_notice_object.save()

        return super(NoticeBoardDetailView, self).get(self, *args, **kwargs)
