from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField


class Anniversary(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = MDTextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    def __str__(self):
        return self.title

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

    class Meta:
        verbose_name = '校庆报道'
        verbose_name_plural = verbose_name
