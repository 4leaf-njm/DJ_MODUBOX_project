from django.forms import ModelForm
from questionapp.models import OrderBoard


class OrderCreationForm(ModelForm):
    class Meta:
        model = OrderBoard
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
        )


