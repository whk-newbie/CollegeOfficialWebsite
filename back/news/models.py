from django.db import models

# Create your models here.
from django.utils import timezone
from markdown import Markdown
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User


class News(models.Model):
    # 用户及权限
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='news_author',
        verbose_name="发布者"
    )
    # 封面
    cover = models.ImageField(upload_to='cover/%Y%m%d', null=True, blank=True, verbose_name="封面")
    title = models.CharField(max_length=100, verbose_name="标题")
    body = MDTextField(verbose_name="文章内容")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="上次更新时间")

    def __str__(self):
        return self.title

    # 新增方法，将 body 转换为带 html 标签的正文
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.tables',
            ]
        )
        md_body = md.convert(self.body)
        return md_body

    class Meta:
        verbose_name = "学院新闻"
        verbose_name_plural = "新闻列表"
