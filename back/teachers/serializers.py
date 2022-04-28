# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/27 20:02 
"""
from rest_framework import serializers

from teachers.models import Teacher, TeacherMorality


class TeacherBaserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherSerializer(TeacherBaserSerializer):
    class Meta(TeacherBaserSerializer.Meta):
        fields = ['id', 'name', 'job_title', 'position', 'degree']


class TeacherDetailSerializer(TeacherBaserSerializer):
    id = serializers.IntegerField(read_only=True)
    personal_profile_html = serializers.SerializerMethodField()

    def get_personal_profile_html(self, obj):
        return obj.get_md()

    class Meta(TeacherBaserSerializer.Meta):
        fields = ['id', 'name', 'job_title', 'position', 'degree', 'personal_profile_html', 'updated']


class TeacherMoralBaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TeacherMorality
        fields = '__all__'


class TeacherMoralitySerializer(TeacherMoralBaseSerializer):
    class Meta(TeacherMoralBaseSerializer.Meta):
        fields = ['id', 'title', 'created']


class TeacherMoralityDetailSerializer(TeacherMoralBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta(TeacherMoralBaseSerializer.Meta):
        fields = ['id', 'title', 'created','content_html']
