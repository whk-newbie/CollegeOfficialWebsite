from django.db import models

# Create your models here.
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User


# 通知模块
class Infos(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='info_author',
        verbose_name='发布者'
    )
    title = models.CharField(max_length=100, verbose_name="标题")
    body = MDTextField(verbose_name="通知内容")
    files = models.FileField(u'文件', upload_to='info/files', default=None, blank=True, null=True)
    time = models.DateTimeField(default=timezone.now,verbose_name="发布时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="上次更新时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "学院通知"
        verbose_name_plural = "通知列表"
