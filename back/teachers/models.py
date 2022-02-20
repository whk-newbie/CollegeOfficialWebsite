from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField


class Teacher(models.Model):
    # 用户及权限
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name="发布者"
    )
    name = models.CharField(max_length=50, verbose_name="姓名")
    email = models.EmailField(max_length=254, verbose_name="邮箱")
    job_title = models.CharField(max_length=50, verbose_name="职称")
    description = MDTextField(verbose_name="个人简介")
    photo = models.ImageField(upload_to='teachers', verbose_name="头像", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    # 新增方法，将 body 转换为带 html 标签的正文
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.description)
        # toc 是渲染后的目录
        return md_body, md.toc

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师信息管理"
        verbose_name_plural = "教师列表"
