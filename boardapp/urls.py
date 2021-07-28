from django.urls import path
from boardapp.views import NoticeBoardListView, NoticeBoardDetailView

app_name = "boardapp"

urlpatterns = [
    path("notice/", NoticeBoardListView.as_view(), name="notice_list"),
    path(
        "notice/<int:pk>",
        NoticeBoardDetailView.as_view(),
        name="notice_detail",
    ),
]
