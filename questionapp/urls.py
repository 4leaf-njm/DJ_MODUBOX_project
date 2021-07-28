from django.urls import path
from questionapp.views import FaqListView, OrderCreateView

app_name = "questionapp"

urlpatterns = [
    path("faq/", FaqListView.as_view(), name="faq"),
    path("order/", OrderCreateView.as_view(), name="order"),
]
