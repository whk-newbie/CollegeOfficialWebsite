from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from party.models import PartyBuilding, PartyFileAndTrends
from party.serializers import PartyBuildingSerializer, PartyBuildingDetailSerializer, PartyFileAndTrendsSerializer, \
    PartyFileAndTrendsDetailSerializer


class PartyBuildingViewSet(viewsets.ModelViewSet):
    queryset = PartyBuilding.objects.all().order_by('-create_time')
    serializer_class = PartyBuildingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PartyBuildingSerializer
        else:
            return PartyBuildingDetailSerializer


class PartyFileAndTrendsViewSet(viewsets.ModelViewSet):
    queryset = PartyFileAndTrends.objects.all().order_by('-create_time')
    serializer_class = PartyFileAndTrendsSerializer

    def get_queryset(self):
        queryset = PartyFileAndTrends.objects.all().order_by('-create_time')
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PartyFileAndTrendsSerializer
        else:
            return PartyFileAndTrendsDetailSerializer
