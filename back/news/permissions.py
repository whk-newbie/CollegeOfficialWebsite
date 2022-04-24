# -*- coding: UTF-8 -*-
"""
@Project ：back 
@File    ：permissions.py
@IDE     ：PyCharm 
@Author  ：whk
@Date    ：2022/4/18 18:36 
"""
from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """

    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD, OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 仅管理员可进行其他操作
        return request.user.is_superuser