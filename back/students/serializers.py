# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/29 10:41 
"""
from rest_framework import serializers

from students.models import Major, Plan, Teaching, Course, Notice, Enrollment, Employment, Learning


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    """
    通过改变Meta.model来实现不同的序列化
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = None
        fields = '__all__'


class MajorSerializer(BaseSerializer):
    class Meta:
        model = Major
        fields = ['id', 'url', 'title', 'create_time']


class MajorDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Major
        fields = ['id', 'title', 'description_html', 'create_time']


class PlanSerializer(BaseSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'url', 'title', 'create_time']


class PlanDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Plan
        fields = ['id', 'title', 'file', 'description_html', 'create_time']


class TeachingSerializer(BaseSerializer):
    class Meta:
        model = Teaching
        fields = ['id', 'url', 'title', 'create_time']


class TeachingDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Teaching
        fields = ['id', 'title', 'file', 'description_html', 'create_time']


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = ['id', 'url', 'title', 'create_time']


class CourseDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Course
        fields = ['id', 'title', 'file', 'description_html', 'create_time']


class NoticeSerializer(BaseSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'url', 'title', 'create_time']


class NoticeDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Notice
        fields = ['id', 'title', 'file', 'description_html', 'create_time']


class EnrollmentSerializer(BaseSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'url', 'title', 'create_time']


class EnrollmentDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Enrollment
        fields = ['id', 'title', 'file', 'description_html', 'create_time']


class EmploymentSerializer(BaseSerializer):
    class Meta:
        model = Employment
        fields = ['id', 'url', 'title', 'create_time']


class EmploymentDetailSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta:
        model = Employment
        fields = ['id', 'title', 'file', 'description_html', 'create_time']


class LearningSerializer(BaseSerializer):
    class Meta:
        model = Learning
        fields = "__all__"
