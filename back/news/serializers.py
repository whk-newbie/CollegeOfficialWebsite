# -*- coding: utf-8 -*-
# @Author  : 王汉坤
# @Time    : 2022/1/24 16:52
# @environment:PyCharm


from rest_framework import serializers
from news.models import News
from userinfo.serializers import UserDescSerializer


class NewsListSerializer(serializers.ModelSerializer):
    """
    News List Serializer
    """
    author = UserDescSerializer(read_only=True)
    # 新增字段，添加超链接
    url = serializers.HyperlinkedIdentityField(view_name="news:detail")

    class Meta:
        model = News
        fields = [
            'url',
            # 'id',
            'title',
            'create_time',
            'author',

        ]


class NewsDetailSerializer(serializers.ModelSerializer):
    """
    News detial serializer
    """
    class Meta:
        model = News
        fields = '__all__'

# class AvatarSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')
#
#     class Meta:
#         model = Avatar
#         fields = '__all__'
