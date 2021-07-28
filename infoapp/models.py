# -*- encoding=UTF-8 -*-

from django.db import models
from core.models import TimeStamped


class FooterInfo(TimeStamped):
    """FooterInfo Model Definition"""

    class Meta:
        verbose_name_plural = "하단정보 관리"

    title = models.CharField(
        "제목", max_length=120, null=False, help_text="푸터에 보일 정보 중 제목 입니다."
    )
    content = models.CharField(
        "내용", max_length=350, null=False, help_text="푸터에 보일 정보 중 내용 입니다."
    )

    def __str__(self):
        return self.title


class LogoInfo(TimeStamped):
    """LogoInfo Model Definition"""

    class Meta:
        verbose_name_plural = "로고정보 관리"

    title = models.CharField(
        "제목", max_length=120, null=False, help_text="푸터에 보일 정보 중 제목 입니다."
    )
    logo_file = models.ImageField(
        "로고파일",
        upload_to="logo/",
        null=False,
        help_text="사이즈에 따라 상이하게 보일 수 있습니다. 업로드 후 화면에서 확인이 필요합니다.",
    )

    def __str__(self):
        return self.title


class AgreementInfo(TimeStamped):
    """AgreementInfo Model Definition"""

    class Meta:
        verbose_name_plural = "약관내용 관리"

    title = models.CharField("제목", max_length=120, null=False)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
