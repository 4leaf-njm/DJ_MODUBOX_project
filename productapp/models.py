from django.db import models
from core.models import TimeStamped


class Product(TimeStamped):
    """Product Model Definition"""

    class Meta:
        verbose_name_plural = "상품/제품 관리"

    PRODUT_TYPE = (
        ("맞춤박스", "맞춤박스"),
        ("쇼핑백", "쇼핑백"),
        ("행택", "행택"),
    )

    title = models.CharField("상품 타이틀", max_length=200, null=False)
    type = models.CharField("상품 유형", choices=PRODUT_TYPE, max_length=100, null=False)
    content = models.TextField("상품 내용")
    spec = models.TextField(
        "제작 사양", null=True, blank=True, help_text="행택의 유형을 선택한 경우에만 적용됩니다."
    )
    sort = models.IntegerField("정렬 순서", help_text="정렬 순서는 3자리 까지 입력 가능합니다.")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image_url = models.ImageField("상품 이미지", upload_to="product/")
    title = models.CharField(max_length=100, null=True, blank=True)
    sort = models.IntegerField("정렬 순서", help_text="정렬 순서는 3자리 까지 입력 가능합니다.")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
