from django.db import models

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    # model이 생성된 날짜
    created = models.DateTimeField(auto_now_add=True)
    # model이 업데이트 될 때마다의 날짜
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True