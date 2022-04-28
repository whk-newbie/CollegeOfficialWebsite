from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from teachers.models import Teacher, TeacherMorality
from teachers.serializers import TeacherSerializer, TeacherDetailSerializer, TeacherMoralitySerializer, \
    TeacherMoralityDetailSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    Could be searcher by name, job title, degree, etc.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        """
        Inquiry according to keywords
        """
        queryset = Teacher.objects.all().order_by('degree')
        name = self.request.query_params.get('name', None)
        position = self.request.query_params.get('position', None)
        degree = self.request.query_params.get('degree', None)
        job_title = self.request.query_params.get('job_title', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if name == "not_null":
            queryset = queryset.filter(name__isnull=False)
        if name == "null":
            queryset = queryset.filter(name__isnull=True)

        if position is not None:
            queryset = queryset.filter(position__icontains=position)
        if position == "not_null":
            queryset = queryset.filter(position__isnull=False)
        if position == "null":
            queryset = queryset.filter(position__isnull=True)

        if degree is not None:
            queryset = queryset.filter(degree__icontains=degree)
        if degree == "not_null":
            queryset = queryset.filter(degree__isnull=False)
        if degree == "null":
            queryset = queryset.filter(degree__isnull=True)

        if job_title is not None:
            queryset = queryset.filter(job_title__icontains=job_title)
        if job_title == "not_null":
            queryset = queryset.filter(job_title__isnull=False)
        if job_title == "null":
            queryset = queryset.filter(job_title__isnull=True)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherSerializer
        else:
            return TeacherDetailSerializer


class TeacherMoralityViewSet(viewsets.ModelViewSet):
    queryset = TeacherMorality.objects.all()
    serializer_class = TeacherMoralitySerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherMoralitySerializer
        else:
            return TeacherMoralityDetailSerializer
