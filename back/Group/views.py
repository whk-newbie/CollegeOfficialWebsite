from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Group.models import GroupNews, Group, Party, System, Honor
from Group.serializers import GroupNewsSerializer, GroupNewsDetailSerializer, GroupSerializer, GroupDetailSerializer, \
    PartySerializer, PartyDetailSerializer, SystemSerializer, SystemDetailSerializer, HonorSerializer, \
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


class SystemViewSet(viewsets.ViewSet):
    queryset = System.objects.all().order_by('-create_time')
    serializer_class = SystemSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SystemSerializer
        else:
            return SystemDetailSerializer


class HonorViewSet(viewsets.ModelViewSet):
    queryset = Honor.objects.all().order_by('-create_time')
    serializer_class = HonorSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return HonorSerializer
        else:
            return HonorDetailSerializer
