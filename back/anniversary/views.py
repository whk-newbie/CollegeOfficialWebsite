from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from anniversary.models import Anniversary
from anniversary.serializers import AnniversarySerializer, AnniversaryDetailSerializer


class AnniversaryViewSet(viewsets.ModelViewSet):
    queryset = Anniversary.objects.all().order_by('-create_time')
    serializer_class = AnniversarySerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AnniversarySerializer
        return AnniversaryDetailSerializer
