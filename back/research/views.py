from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from research.models import Research, institutions, achievements
from research.serializers import ResearchSerializer, ResearchDetailSerializer, InstitutionsSerializer, \
    InstitutionsDetailSerializer, AchievementsSerializer, AchievementsDetailSerializer


class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all().order_by('-date')
    serializer_class = ResearchSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ResearchSerializer
        else:
            return ResearchDetailSerializer


class InstitutionsViewSet(viewsets.ModelViewSet):
    queryset = institutions.objects.all().order_by('-date')
    serializer_class = InstitutionsSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return InstitutionsSerializer
        else:
            return InstitutionsDetailSerializer


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = achievements.objects.all().order_by('-date')
    serializer_class = AchievementsSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AchievementsSerializer
        else:
            return AchievementsDetailSerializer
