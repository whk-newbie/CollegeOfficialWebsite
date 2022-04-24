from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from information.models import Information
from information.serializers import InformationSerializer, InformationDetailSerializer
from News.permissions import IsAdminUserOrReadOnly


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all().order_by('pub_time')
    serializer_class = InformationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return InformationSerializer
        else:
            return InformationDetailSerializer
