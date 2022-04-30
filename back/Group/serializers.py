# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/30 14:37 
"""
from rest_framework import serializers

from Group.models import GroupNews, Group, Party, System, Honor


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = None
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class BaseDetailGroupSerializer(serializers.ModelSerializer):
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


class GroupNewsDetailSerializer(BaseDetailGroupSerializer):
    class Meta:
        model = GroupNews
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class GroupSerializer(BaseDetailGroupSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class GroupDetailSerializer(BaseDetailGroupSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class PartySerializer(BaseSerializer):
    class Meta:
        model = Party
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class PartyDetailSerializer(BaseDetailGroupSerializer):
    class Meta:
        model = Party
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class SystemSerializer(BaseSerializer):
    class Meta:
        model = System
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class SystemDetailSerializer(BaseDetailGroupSerializer):
    class Meta:
        model = System
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']


class HonorSerializer(BaseSerializer):
    class Meta:
        model = Honor
        fields = ['id', 'url', 'title', 'create_time', 'update_time']


class HonorDetailSerializer(BaseDetailGroupSerializer):
    class Meta:
        model = Honor
        fields = ['id', 'title', 'create_time', 'update_time', 'desc_html']
