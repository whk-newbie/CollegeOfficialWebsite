# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/30 9:42 
"""
from rest_framework import serializers

from party.models import PartyBuilding, PartyFileAndTrends
from students.serializers import BaseSerializer


class PartyBuildingSerializer(BaseSerializer):
    class Meta:
        model = PartyBuilding
        fields = ['id', 'url', 'title', 'create_time']


class PartyBuildingDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = PartyBuilding
        fields = ['id', 'title', 'create_time', 'content_html']


class PartyFileAndTrendsSerializer(BaseSerializer):
    class Meta:
        model = PartyFileAndTrends
        fields = ['id', 'url', 'title', 'create_time']


class PartyFileAndTrendsDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = PartyFileAndTrends
        fields = ['id', 'title', 'create_time', 'content_html']
