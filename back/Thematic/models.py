from django.db import models

# Create your models here.

# base model
from markdown import Markdown
from mdeditor.fields import MDTextField


class BasemodelOfTH(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='标题')
    content = MDTextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        abstract = True

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.tables',
            ]
        )
        md_body = md.convert(self.content)
        return md_body

    def __str__(self):
        return self.title


class report(BasemodelOfTH):
    class Meta:
        verbose_name = '活动报道'
        verbose_name_plural = verbose_name


class infos(BasemodelOfTH):
    class Meta:
        verbose_name = '通知公告'
        verbose_name_plural = verbose_name


class filelearn(BasemodelOfTH):
    class Meta:
        verbose_name = '文件学习'
        verbose_name_plural = verbose_name
