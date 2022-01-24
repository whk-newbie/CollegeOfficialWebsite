# -*- coding: utf-8 -*-
# @Author  : 王汉坤
# @Time    : 2022/1/24 17:42
# @environment:PyCharm

from django.contrib.auth.models import User
from rest_framework import serializers


class UserDescSerializer(serializers.ModelSerializer):
    """于文章列表中引用的嵌套序列化器"""

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'date_joined'
        ]
