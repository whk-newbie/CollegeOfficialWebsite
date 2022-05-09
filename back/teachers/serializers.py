# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/27 20:02 
"""
from rest_framework import serializers

from teachers.models import Teacher, TeacherMorality, recruiting
from students.serializers import BaseSerializer


class TeacherSerializer(BaseSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'url', 'name', 'job_title', 'position', 'degree']


class TeacherDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)

    personal_profile_html = serializers.SerializerMethodField()

    def get_personal_profile_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'photo', 'job_title', 'position', 'degree', 'personal_profile_html', 'updated']


class TeacherMoralitySerializer(BaseSerializer):
    class Meta:
        model = TeacherMorality
        fields = ['id', 'title', 'create_time']


class TeacherMoralityDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)

    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = TeacherMorality
        fields = ['id', 'title', 'content_html', 'create_time']


class RecruitingSerializer(BaseSerializer):
    class Meta:
        model = recruiting
        fields = ['id', 'title', 'create_time']


class RecruitingDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)

    content_html = serializers.SerializerMethodField()

    def get_content_html(self, obj):
        return obj.get_md()

    class Meta:
        model = recruiting
        fields = ['id', 'title', 'content_html', 'create_time']

# class TeacherBaserSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Teacher
#         fields = '__all__'


# class TeacherSerializer(TeacherBaserSerializer):
#     class Meta(TeacherBaserSerializer.Meta):
#         fields = ['id', 'name', 'job_title', 'position', 'degree']
#
#
# class TeacherDetailSerializer(TeacherBaserSerializer):
#     id = serializers.IntegerField(read_only=True)
#     personal_profile_html = serializers.SerializerMethodField()
#
#     def get_personal_profile_html(self, obj):
#         return obj.get_md()
#
#     class Meta(TeacherBaserSerializer.Meta):
#         fields = ['id', 'name', 'job_title', 'position', 'degree', 'personal_profile_html', 'updated']
#
#
# class TeacherMoralBaseSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = TeacherMorality
#         fields = '__all__'
#
#
# class TeacherMoralitySerializer(TeacherMoralBaseSerializer):
#     class Meta(TeacherMoralBaseSerializer.Meta):
#         fields = ['id', 'title', 'create_time']
#
#
# class TeacherMoralityDetailSerializer(TeacherMoralBaseSerializer):
#     id = serializers.IntegerField(read_only=True)
#     content_html = serializers.SerializerMethodField()
#
#     def get_content_html(self, obj):
#         return obj.get_md()
#
#     class Meta(TeacherMoralBaseSerializer.Meta):
#         fields = ['id', 'title', 'create_time', 'content_html']
#
#
# class RecuitingBaseSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = recruiting
#         fields = '__all__'
#
#
# class RecuitingSerializer(RecuitingBaseSerializer):
#     class Meta(RecuitingBaseSerializer.Meta):
#         fields = ['id', 'title', 'create_time']
#
#
# class RecuitingDetailSerializer(RecuitingBaseSerializer):
#     id = serializers.IntegerField(read_only=True)
#     content_html = serializers.SerializerMethodField()
#
#     def get_content_html(self, obj):
#         return obj.get_md()
#
#     class Meta(RecuitingBaseSerializer.Meta):
#         fields = ['id', 'title', 'create_time', 'content_html']
