# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/29 10:41 
"""
from rest_framework import serializers

from students.models import Major


class MajorBaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Major
        fields = '__all__'


class MajorSerializer(MajorBaseSerializer):
    class Meta(MajorBaseSerializer.Meta):
        fields = ['id', 'name', 'create_time']


class MajorDetailSerializer(MajorBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta(MajorBaseSerializer.Meta):
        fields = ['id', 'name', 'description_html', 'create_time']
