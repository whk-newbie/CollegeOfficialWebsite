from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField


class Teacher(models.Model):
    """
    Teachers model
    """
    name = models.CharField(max_length=20, verbose_name="姓名")  # teacher name

    title_choices = (('特聘教授', '特聘教授'), ('教授', '教授'), ('副教授', '副教授'), ('讲师', '讲师'), ('助教', '助教'), ('其他', '其他'))
    job_title = models.CharField(max_length=50, blank=True, choices=title_choices,
                                 verbose_name="职称")  # teacher job title

    degree_choices = (('博士', '博士'), ('硕士', '硕士'), ('学士', '学士'), ('其他', '其他'))
    degree = models.CharField(max_length=20, blank=True, choices=degree_choices, verbose_name="学位")  # teacher degree

    position_choces = (('院长', '院长'), ('副院长', '副院长'), ('研究员', '研究员'), ('副研究员', '副研究员'), ('助理研究员', '助理研究员'), ('其他', '其他'))
    position = models.CharField(max_length=50, blank=True, choices=position_choces,
                                verbose_name="职务")  # teacher position

    personal_profile = MDTextField(verbose_name="个人简介")  # teacher personal profile
    photo = models.ImageField(upload_to='teachers/', blank=True, verbose_name="教师图片")  # teacher photo
    created = models.DateTimeField(auto_now_add=True)  # create time
    updated = models.DateTimeField(auto_now=True)  # update time

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.personal_profile)
        # toc 是渲染后的目录
        return md_body

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name


class TeacherMorality(models.Model):
    """
    Teacher morality model
    """
    title = models.CharField(max_length=50, verbose_name="标题")  # morality title
    content = MDTextField(verbose_name="文章内容")
    created = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")  # create time

    def __str__(self):
        return self.title

    # 新增方法，将 body 转换为带 html 标签的正文
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.content)
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = "师德师风建设"
        verbose_name_plural = verbose_name
