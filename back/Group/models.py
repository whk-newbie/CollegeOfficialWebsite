from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField


class BaseModel(models.Model):
    """
    BaseModel
    """
    title = models.CharField(max_length=100, verbose_name='标题')
    desc = MDTextField(verbose_name='文章内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

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
        md_body = md.convert(self.desc)
        return md_body

    def __str__(self):
        return self.title


# 学工新闻
class GroupNews(BaseModel):
    """
    News
    """

    class Meta:
        verbose_name = '学工新闻'
        verbose_name_plural = verbose_name


# 团学组织
class Group(BaseModel):
    """
    Group
    """

    class Meta:
        verbose_name = '团学组织'
        verbose_name_plural = verbose_name


# 党员服务
class Party(BaseModel):
    """
    Party
    """

    class Meta:
        verbose_name = '党员服务'
        verbose_name_plural = verbose_name


# 管理制度
class Management(BaseModel):
    """
    Management
    """

    class Meta:
        verbose_name = '管理制度'
        verbose_name_plural = verbose_name


# 荣誉室
class Honor(BaseModel):
    """
    Honor
    """
    photo = models.ImageField(upload_to='honor', verbose_name='封面图片', null=True, blank=True, default=None)
    file = models.FileField(upload_to='honor/%Y/%m', verbose_name='文件', blank=True, null=True)

    class Meta:
        verbose_name = '荣誉室'
        verbose_name_plural = verbose_name
