from django.db import models
from core.models import TimeStamped


class MainBanner(TimeStamped):
    """MainBanner Model Definitions"""

    class Meta:
        verbose_name_plural = "메인베너 관리"

    image_file = models.ImageField(
        "베너 이미지",
        upload_to="banner/",
        help_text="이미지 사이즈에 따라 화면에 상이하게 보일 수 있기 때문에 업로드 및 수정 후 화면 확인이 필요합니다.",
    )
    mobile_image_file = models.ImageField(
        "모바일_베너 이미지",
        upload_to="banner/",
        help_text="이미지 사이즈에 따라 화면에 상이하게 보일 수 있기 때문에 업로드 및 수정 후 화면 확인이 필요합니다.",
        null=True,
    )
    title = models.CharField("타이틀", max_length=200, null=True)
    content = models.TextField("베너 내용", null=True)
    sort = models.IntegerField("정렬순서", default=1)

    def __str__(self):
        return self.title
