from django.db import models

# Create your models here.
from markdown import Markdown
from mdeditor.fields import MDTextField

choices = (('本科生', '本科生'), ('研究生', '研究生'), ('博士生', '博士生'))


# 专业介绍
class Major(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='专业名称')
    category = models.CharField(max_length=20, choices=choices, verbose_name='学生类别')
    description = MDTextField(max_length=200, blank=True, verbose_name='专业介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

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
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '专业介绍'
        verbose_name_plural = verbose_name


# 培养方案
class Plan(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='培养方案名称')
    category = models.CharField(max_length=20, choices=choices, verbose_name='学生类别')
    file = models.FileField(upload_to='student/plan/', blank=True, verbose_name='培养方案文件')
    description = MDTextField(max_length=200, blank=True, verbose_name='培养方案介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

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
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '培养方案'
        verbose_name_plural = verbose_name


# 教学成果
class Teaching(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='教学成果名称')
    category = models.CharField(max_length=20, choices=choices, verbose_name='学生类别', default='本科生')
    file = models.FileField(upload_to='student/teaching/', blank=True, verbose_name='教学成果文件')
    description = MDTextField(max_length=200, blank=True, verbose_name='教学成果介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

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
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '教学成果'
        verbose_name_plural = verbose_name


# 精品课程
class Course(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='精品课程名称')
    category = models.CharField(max_length=20, choices=choices, default='本科生', verbose_name='学生类别')
    file = models.FileField(upload_to='student/course/', blank=True, verbose_name='精品课程文件')
    description = MDTextField(max_length=200, blank=True, verbose_name='精品课程介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

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
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '精品课程'
        verbose_name_plural = verbose_name


# 研究生信息公告
class Notice(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="标题")
    category = models.CharField(max_length=20, choices=choices, default='研究生', verbose_name='学生类别')
    file = models.FileField(upload_to='student/notice/', blank=True, verbose_name='文件')
    description = MDTextField(max_length=200, blank=True, verbose_name='文字介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        md_body = md.convert(self.description)
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '研究生信息公告'
        verbose_name_plural = verbose_name


# 招生
class Enrollment(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="标题")
    category = models.CharField(max_length=20, choices=choices, default='研究生', verbose_name='学生类别')
    file = models.FileField(upload_to='student/Enrollment/', blank=True, verbose_name='文件')
    description = MDTextField(max_length=200, blank=True, verbose_name='文字介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        md_body = md.convert(self.description)
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '学院招生'
        verbose_name_plural = verbose_name


# 学生就业
class Employment(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="标题")
    category = models.CharField(max_length=20, choices=choices, default='研究生', verbose_name='学生类别')
    file = models.FileField(upload_to='student/job/', blank=True, verbose_name='文件')
    description = MDTextField(max_length=200, blank=True, verbose_name='文字介绍')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        md_body = md.convert(self.description)
        # toc 是渲染后的目录
        return md_body

    class Meta:
        verbose_name = '学生就业'
        verbose_name_plural = verbose_name
