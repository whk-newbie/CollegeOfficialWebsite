# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/5/15 16:21 
"""
from rest_framework import serializers
from MSboard.models import board


class BoardSerializer(serializers.ModelSerializer):
    """
    MSBoard Serializer
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = board
        fields = '__all__'

