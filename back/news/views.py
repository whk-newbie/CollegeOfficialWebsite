from django.shortcuts import render

# Create your views here.

from News.models import News
from News.serializers import NewsDetailSerializer, NewsSerializer
from rest_framework import viewsets
from News.permissions import IsAdminUserOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-create_time')
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return NewsSerializer
        else:
            return NewsDetailSerializer


