"""
The Teachers Serializers
"""

from rest_framework import serializers
from userinfo.serializers import UserDescSerializer
from .models import Teacher


class TeacherListSerializer(serializers.ModelSerializer):
    """
    The Teacher List Serializer
    """
    author = UserDescSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="teachers:detail")
    class Meta:
        model = Teacher
        fields = ('url', 'name', 'job_title', 'updated','author')


class TeacherDetailSerializer(serializers.ModelSerializer):
    """
    The Teacher Serializer
    """

    class Meta:
        model = Teacher
        fields = '__all__'

