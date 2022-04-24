# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/24 17:26 
"""
from rest_framework import serializers
from information.models import Information


class InformationBaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Information
        fields = '__all__'


class InformationSerializer(InformationBaseSerializer):
    class Meta:
        model = Information
        fields = '__all__'
        extra_kwargs = {'content': {'write_only': True}}


class InformationDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # author = serializers.CharField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md_content()

    class Meta:
        model = Information
        fields = ['id', 'title', 'file', 'content_html', 'pub_time']
