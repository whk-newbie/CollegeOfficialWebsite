# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/29 10:41 
"""
from rest_framework import serializers

from students.models import Major, Plan, Teaching, Course


class MajorBaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Major
        fields = '__all__'


class MajorSerializer(MajorBaseSerializer):
    class Meta(MajorBaseSerializer.Meta):
        model = Major
        fields = ['id', 'name', 'create_time']


class MajorDetailSerializer(MajorBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta(MajorBaseSerializer.Meta):
        model = Major
        fields = ['id', 'name', 'description_html', 'create_time']


class PlanBaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Plan
        fields = '__all__'


class PlanSerializer(PlanBaseSerializer):
    class Meta(PlanBaseSerializer.Meta):
        model = Plan
        fields = ['id', 'name', 'create_time']


class PlanDetailSerializer(PlanBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta(PlanBaseSerializer.Meta):
        model = Plan
        fields = ['id', 'name', 'file', 'description_html', 'create_time']


class TeachingBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Teaching
        fields = '__all__'


class TeachingSerializer(TeachingBaseSerializer):
    class Meta(TeachingBaseSerializer.Meta):
        model = Teaching
        fields = ['id', 'name', 'create_time']


class TeachingDetailSerializer(TeachingBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta(TeachingBaseSerializer.Meta):
        model = Teaching
        fields = ['id', 'name', 'file', 'description_html', 'create_time']


class CourseBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseSerializer(CourseBaseSerializer):
    class Meta(CourseBaseSerializer.Meta):
        model = Course
        fields = ['id', 'name', 'create_time']


class CourseDetailSerializer(CourseBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    description_html = serializers.SerializerMethodField()

    def get_description_html(self, obj):
        return obj.get_md()

    class Meta(CourseBaseSerializer.Meta):
        model = Course
        fields = ['id', 'name', 'file', 'description_html', 'create_time']
