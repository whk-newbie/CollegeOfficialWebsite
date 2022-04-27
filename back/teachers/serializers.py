# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/27 20:02 
"""
from rest_framework import serializers

from teachers.models import Teacher


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
        fields = ['id', 'name', 'personal_profile_html']
