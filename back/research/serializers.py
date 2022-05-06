# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@create_time    ：2022/4/29 20:48 
"""
from rest_framework import serializers

from research.models import Research, institutions
from students.serializers import BaseSerializer


class ResearchSerializer(BaseSerializer):
    class Meta:
        model = Research
        fields = ['id', 'url', 'title', 'create_time']


class ResearchDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Research
        fields = ['id', 'title', 'create_time', 'content_html', 'file']


class InstitutionsSerializer(BaseSerializer):
    class Meta:
        model = institutions
        fields = ['id', 'url', 'title', 'create_time']


class InstitutionsDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = institutions
        fields = ['id', 'title', 'create_time', 'content_html']


class AchievementsSerializer(BaseSerializer):
    class Meta:
        model = institutions
        fields = ['id', 'url', 'title', 'create_time']


class AchievementsDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = institutions
        fields = ['id', 'title', 'create_time', 'content_html', 'file']
