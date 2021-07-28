from django.contrib import admin
from productapp.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    """Product Image Tabular Definition"""

    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    inlines = (ProductImageInline,)

    list_display = (
        "title",
        "type",
        "sort",
        "updated",
        "created",
    )

    list_filter = ("type",)

    fields = (
        "title",
        "type",
        "spec",
        "sort",
        "updated",
        "created",
    )

    readonly_fields = (
        "updated",
        "created",
    )
