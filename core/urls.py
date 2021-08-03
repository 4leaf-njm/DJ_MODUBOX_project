from django.urls import path
from core.views import HomeView, DesignView, ProcessingView, GallaryView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("design/", DesignView.as_view(), name="design"),
    path("processing/", ProcessingView.as_view(), name="processing"),
    path("gallary/", GallaryView.as_view(), name="gallary"),
]
