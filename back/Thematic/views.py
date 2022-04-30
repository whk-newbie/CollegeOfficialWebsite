from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Thematic.serializers import ReportSerializer, ReportDetailSerializer, InfosSerializer, InfosDetailSerializer, \
    FilelearnSerializer, FilelearnDetailSerializer
from .models import report, infos, filelearn


class ReportViewSet(viewsets.ModelViewSet):
    queryset = report.objects.all().order_by('-create_time')
    serializer_class = ReportSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ReportSerializer
        else:
            return ReportDetailSerializer


class InfosViewSet(viewsets.ModelViewSet):
    queryset = infos.objects.all().order_by('-create_time')
    serializer_class = InfosSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return InfosSerializer
        else:
            return InfosDetailSerializer


class FilelearnViewSet(viewsets.ModelViewSet):
    queryset = filelearn.objects.all().order_by('-create_time')
    serializer_class = FilelearnSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return FilelearnSerializer
        else:
            return FilelearnDetailSerializer
