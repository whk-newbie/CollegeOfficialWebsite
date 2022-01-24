# -*- coding: utf-8 -*-
# @Author  : 王汉坤
# @Time    : 2022/1/24 18:24
# @environment:PyCharm


from rest_framework import serializers
from imagenews.models import Avatar, ImageNews
from userinfo.serializers import UserDescSerializer


class ImageNewsListSerializer(serializers.ModelSerializer):
    author = UserDescSerializer(read_only=True)
    # 新增字段，添加超链接
    url = serializers.HyperlinkedIdentityField(view_name="article:detail")

    class Meta:
        model = ImageNews
        fields = [
            'url',
            # 'id',
            'title',
            'create_time',
            'author',

        ]


class ImageNewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = '__all__'

# class AvatarSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')
#
#     class Meta:
#         model = Avatar
#         fields = '__all__'
