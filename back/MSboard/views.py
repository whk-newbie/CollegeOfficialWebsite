from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from MSboard.models import board
from MSboard.serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = board.objects.all()
    serializer_class = BoardSerializer
