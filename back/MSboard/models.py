from django.db import models


# Create your models here.


class board(models.Model):
    """
    message board
    """
    who = models.CharField(max_length=20, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='地址')
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_reply = models.BooleanField(default=False, verbose_name='是否回复')

    # 意见回复

    def __str__(self):
        return self.title

