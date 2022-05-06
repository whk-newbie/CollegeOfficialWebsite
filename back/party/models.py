from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField


class PartyBuilding(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = MDTextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
            ]
        )
        md_body = md.convert(self.content)
        return md_body

    class Meta:
        verbose_name = '党建工作'
        verbose_name_plural = verbose_name


class PartyFileAndTrends(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    category = models.CharField(max_length=100, verbose_name='分类', choices=(('教育文件', '教育文件'), ('学习动态', '学习动态')))
    content = MDTextField(verbose_name='内容')
    file = models.FileField(upload_to='party/files/', blank=True, verbose_name='文件')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
            ]
        )
        md_body = md.convert(self.content)
        return md_body

    class Meta:
        verbose_name = '党史教育文件及动态'
        verbose_name_plural = verbose_name


