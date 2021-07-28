from django.db import models


class TimeStamped(models.Model):
    """TimestampledModel Definition"""

    created = models.DateTimeField("작성일", auto_now_add=True)
    updated = models.DateTimeField("수정일", auto_now=True)

    class Meta:
        abstract = True
