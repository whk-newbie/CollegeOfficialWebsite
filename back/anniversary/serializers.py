# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/5/17 14:53 
"""
from rest_framework import serializers
from anniversary.models import Anniversary
from students.serializers import BaseSerializer


class AnniversarySerializer(BaseSerializer):
    class Meta:
        model = Anniversary
        fields = ['id', 'url', 'title', 'create_time']


class AnniversaryDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Anniversary
        fields = ['id', 'title', 'content_html', 'create_time']
