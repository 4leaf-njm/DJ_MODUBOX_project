from django.urls import path
from productapp.views import ProductListView

app_name = "product"

urlpatterns = [
    path("intro/<int:type>", ProductListView.as_view(), name="list"),
]
