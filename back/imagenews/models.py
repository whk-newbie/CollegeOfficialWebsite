from django.db import models

# Create your models here.
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User


# 学院新闻模块
class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class ImageNews(models.Model):
    # 用户及权限
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='imagenews',
        verbose_name="发布者"
    )
    # 标题图/图片
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='imgaenews',
        verbose_name="封面图片"
    )
    title = models.CharField(max_length=100, verbose_name="标题")
    body = MDTextField(verbose_name="文章内容")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="上次更新时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "图片新闻"
        verbose_name_plural = "图片列表"
