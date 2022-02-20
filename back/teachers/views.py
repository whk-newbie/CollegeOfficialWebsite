from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from news.permissions import IsAdminUserOrReadOnly
from teachers.models import Teacher
from teachers.serializers import TeacherListSerializer, TeacherDetailSerializer

"""
Teachers views
"""


class TeachersListView(generics.ListCreateAPIView):
    """
    List all teachers
    """
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer


class TeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a teacher instance
    """
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
