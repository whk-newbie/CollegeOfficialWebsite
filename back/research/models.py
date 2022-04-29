from django.db import models

# Create your models here.

# 科研动态
from markdown import Markdown
from mdeditor.fields import MDTextField


class Research(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = MDTextField(blank=True, verbose_name='内容')
    file = models.FileField(upload_to='research/files/', blank=True, null=True, verbose_name='文件')
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        md_body = md.convert(self.content)
        return md_body

    class Meta:
        verbose_name = '科研动态'
        verbose_name_plural = verbose_name


# 科研机构
class institutions(models.Model):
    name = models.CharField(max_length=100, verbose_name='机构名称')
    logo = models.ImageField(upload_to='research/institutions/', blank=True, null=True, verbose_name='机构logo')
    description = MDTextField(blank=True, null=True, verbose_name='简介')
    date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        md_body = md.convert(self.description)
        return md_body

    class Meta:
        verbose_name = '科研机构'
        verbose_name_plural = verbose_name


# 　科研成果
class achievements(models.Model):
    name = models.CharField(max_length=100, verbose_name='成果名称')
    description = MDTextField(blank=True, null=True, verbose_name='简介')
    file = models.FileField(upload_to='research/achievements/', blank=True, null=True, verbose_name='文件')
    date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        md_body = md.convert(self.description)
        return md_body

    class Meta:
        verbose_name = '科研成果'
        verbose_name_plural = verbose_name
