from django.shortcuts import render
from core.views import CustomListView, CustomCreateView
from questionapp.models import QnaBoard, OrderBoard
from questionapp.forms import OrderCreationForm
from django.urls import reverse


class OrderCreateView(CustomCreateView):
    model = OrderBoard
    form_class = OrderCreationForm
    template_name = "questionapp/order_create.html"

    def get_success_url(self):
        return reverse("core:home")


class FaqListView(CustomListView):
    model = QnaBoard
    template_name = "questionapp/faq_list.html"
    context_object_name = "faq_list"

    def get_queryset(self):

        search_value = self.request.GET.get("search")

        if search_value == None or search_value == "전체":
            return super().get_queryset()
        else:

            new_model = QnaBoard.objects.filter(type=search_value)
            return new_model

    def get_context_data(self, **kwargs):
        context = super(FaqListView, self).get_context_data(**kwargs)

        all_object = QnaBoard.objects.all().order_by("type")
        type_list = []

        for obj in all_object:
            type_list.append(obj.type)

        type_list = list(set(type_list))
        context["type_list"] = type_list

        return context
