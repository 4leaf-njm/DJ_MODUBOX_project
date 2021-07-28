from django.db import models
from django.db.models.fields import DateField, DateTimeField
from core.models import TimeStamped
from userapp.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime


class NoticeBoard(TimeStamped):

    """NoticeBoard Model Definition"""

    title = models.CharField("제목", max_length=200, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자", related_name="user"
    )
    content = RichTextUploadingField(blank=True, null=True)
    hit = models.IntegerField("조회수", default=0)

    asdflkasdklf = models.CharField(max_length=30, null=True)
    asdflkasdklf22 = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name_plural = "공지사항 관리"

    def __str__(self):
        return f"{self.title}"


class NoticeFile(models.Model):
    """NoticeFile Model Definition"""

    file = models.FileField(upload_to="boardfiles/", null=True)
    notice = models.ForeignKey(
        NoticeBoard, on_delete=models.CASCADE, related_name="files"
    )

    def __str__(self):
        return f"첨부파일_{self.pk}"


class EventBoard(TimeStamped):
    """EventBoard Model Definition"""

    width_px = "300"
    height_px = "300"

    thumbnail = models.ImageField(
        "썸네일",
        upload_to="event/",
        null=False,
        default=f"https://via.placeholder.com/{width_px}x{height_px}/ffffff?text={width_px}x{height_px}",
        help_text=f"썸네일은 필수 입니다. 사이즈는 px을 기준으로 하며 {width_px} x {height_px} 입니다.",
    )
    title = models.CharField("제목", max_length=200, null=False, default="제목없음")
    content = RichTextUploadingField(blank=True, null=True)
    hit = models.IntegerField("조회수", default=0)
    event_start_date = DateField(default=datetime.now, blank=True)
    event_end_date = DateField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "이벤트 관리"

    def __str__(self):
        return f"{self.title}"
