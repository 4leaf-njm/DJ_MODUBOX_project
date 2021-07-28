from django.shortcuts import render
from core.views import CustomListView
from productapp.models import Product


class ProductListView(CustomListView):
    model = Product
    context_object_name = "product_list"
    template_name = "productapp/product_list.html"

    def get_queryset(self):

        product_type = self.kwargs["type"]

        if product_type == 1:
            result_product = Product.objects.filter(type="맞춤박스")
            return result_product
        elif product_type == 2:
            result_product = Product.objects.filter(type="쇼핑백")
            return result_product
        elif product_type == 3:
            result_product = Product.objects.filter(type="행택")
            return result_product
        else:
            result_product = Product.objects.filter(type="맞춤박스")
            return result_product
