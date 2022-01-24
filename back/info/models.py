from django.db import models

# Create your models here.
from django.utils import timezone
from mdeditor.fields import MDTextField


# 通知模块
class Infos(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    body = MDTextField(verbose_name="通知内容")
    files = models.FileField(u'文件', upload_to='info/files', default=None, blank=False)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "学院通知"
        verbose_name_plural = "通知列表"
