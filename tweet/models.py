from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(verbose_name='テキスト', max_length=140)
    created_at = models.DateTimeField(verbose_name='投稿日時', default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
