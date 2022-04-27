from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField


class Teacher(models.Model):
    """
    Teachers model
    """
    name = models.CharField(max_length=20, verbose_name="姓名")  # teacher name

    title_choices = ((0, '特聘教授'), (1, '教授'), (2, '副教授'), (3, '讲师'), (4, '助教'), (5, '副研究员'))
    job_title = models.CharField(max_length=50, blank=True, choices=title_choices,
                                 verbose_name="职称")  # teacher job title

    degree_choices = ((0, '博士'), (1, '硕士'), (2, '学士'), (3, '其他'))
    degree = models.CharField(max_length=50, choices=degree_choices, verbose_name="学位")  # teacher degree

    personal_profile = MDTextField(verbose_name="个人简介")  # teacher personal profile
    photo = models.ImageField(upload_to='teachers/', blank=True, verbose_name="教师图片")  # teacher photo
    created = models.DateTimeField(auto_now_add=True)  # create time
    updated = models.DateTimeField(auto_now=True)  # update time

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
