from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User


class Information(models.Model):
    """
    通知models
    """
    # 用户及权限
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='info_author',
        verbose_name="发布者",
        default=1
    )

    title = models.CharField(max_length=100, verbose_name="标题")
    content = MDTextField(blank=True, verbose_name="内容")
    file = models.FileField(upload_to="information/%Y%m%d", verbose_name="通知文件", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    class Meta:
        verbose_name = "学院通知"
        verbose_name_plural = verbose_name

    def get_md_content(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.tables',
            ]
        )
        return md.convert(self.content)

    def __str__(self):
        return self.title
