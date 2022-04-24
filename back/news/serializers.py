# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/18 18:33 
"""
from rest_framework import serializers

from News.models import News
from userinfo.serializers import UserDescSerializer


class NewsBaseSerializer(serializers.HyperlinkedModelSerializer):
    """
    新闻基础序列化
    """
    id = serializers.IntegerField(read_only=True)
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class NewsSerializer(NewsBaseSerializer):
    """
    新闻序列化器
    """

    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}


class NewsDetailSerializer(NewsBaseSerializer):
    """
    News detial serializer
    """
    id = serializers.IntegerField(read_only=True)
    author = UserDescSerializer(read_only=True)
    body_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()

    class Meta:
        model = News
        fields = ['id', 'title', 'body_html', 'author', 'create_time', 'update_time']
