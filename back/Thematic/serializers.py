# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/30 18:57 
"""
from rest_framework import serializers

from Thematic.models import report, infos, filelearn


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = None
        fields = ['id', 'url', 'title', 'create_time']


class BaseDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = None
        fields = ['id', 'title', 'create_time', 'update_time', 'content_html']


class ReportSerializer(BaseSerializer):
    class Meta:
        model = report
        fields = ['id', 'url', 'title', 'create_time']


class ReportDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = report
        fields = ['id', 'title', 'create_time', 'content_html']


class InfosSerializer(BaseSerializer):
    class Meta:
        model = infos
        fields = ['id', 'url', 'title', 'create_time']


class InfosDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = infos
        fields = ['id', 'title', 'create_time', 'content_html']


class FilelearnSerializer(BaseSerializer):
    class Meta:
        model = filelearn
        fields = ['id', 'url', 'title', 'create_time']


class FilelearnDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = filelearn
        fields = ['id', 'title', 'create_time', 'content_html']
