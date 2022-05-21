from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Group.models import GroupNews, Group, Party, Management, Honor
from Group.serializers import GroupNewsSerializer, GroupNewsDetailSerializer, GroupSerializer, GroupDetailSerializer, \
    PartySerializer, PartyDetailSerializer, ManagementSerializer, ManagementDetailSerializer, HonorSerializer, \
    HonorDetailSerializer


class GroupNewsViewSet(viewsets.ModelViewSet):
    queryset = GroupNews.objects.all().order_by('-create_time')
    serializer_class = GroupNewsSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return GroupNewsSerializer
        else:
            return GroupNewsDetailSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-create_time')
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return GroupSerializer
        else:
            return GroupDetailSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('-create_time')
    serializer_class = PartySerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PartySerializer
        else:
            return PartyDetailSerializer


class ManagementViewSet(viewsets.ViewSet):
    queryset = Management.objects.all().order_by('-create_time')
    serializer_class = ManagementSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ManagementSerializer
        else:
            return ManagementDetailSerializer


class HonorViewSet(viewsets.ModelViewSet):
    queryset = Honor.objects.all().order_by('-create_time')
    serializer_class = HonorSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return HonorSerializer
        else:
            return HonorDetailSerializer

    def get_queryset(self):
        queryset = Honor.objects.all().order_by('-create_time')
        # 查询参数带有photo的方位photo不为空的数据
        ptoto = self.request.query_params.get('photo', None)
        if ptoto is not None:
            queryset = queryset.exclude(photo='')

        return queryset
