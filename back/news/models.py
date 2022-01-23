from django.db import models

# Create your models here.
from django.utils import timezone
from mdeditor.fields import MDTextField


# 学院新闻模块
class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class News(models.Model):
    # 标题图
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='News'
    )
    title = models.CharField(max_length=100)
    body = MDTextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
