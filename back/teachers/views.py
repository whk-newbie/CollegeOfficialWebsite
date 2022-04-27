from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer, TeacherDetailSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    Could be searcher by name, job title, degree, etc.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned teachers to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Teacher.objects.all()
        username = self.request.query_params.get('name', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        degree = self.request.query_params.get('degree', None)
        if degree is not None:
            queryset = queryset.filter(degree=degree)
        job_title = self.request.query_params.get('title', None)
        if job_title is not None:
            queryset = queryset.filter(job_title=job_title)
        position = self.request.query_params.get('position', None)
        if position is not None:
            queryset = queryset.filter(position=position)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherSerializer
        else:
            return TeacherDetailSerializer
