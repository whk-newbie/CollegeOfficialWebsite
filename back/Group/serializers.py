# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/30 14:37 
"""
from rest_framework import serializers

from Group.models import GroupNews, Group, Party, Management, Honor


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = None
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class BaseDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    desc_html = serializers.SerializerMethodField()

    def get_desc_html(self, obj):
        return obj.get_md()

    class Meta:
        model = None
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class GroupNewsSerializer(BaseSerializer):
    class Meta:
        model = GroupNews
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class GroupNewsDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = GroupNews
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class GroupSerializer(BaseDetailSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class GroupDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class PartySerializer(BaseSerializer):
    class Meta:
        model = Party
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class PartyDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = Party
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class ManagementSerializer(BaseSerializer):
    class Meta:
        model = Management
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class ManagementDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = Management
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class HonorSerializer(BaseSerializer):
    class Meta:
        model = Honor
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class HonorDetailSerializer(BaseDetailSerializer):
    class Meta:
        model = Honor
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']
