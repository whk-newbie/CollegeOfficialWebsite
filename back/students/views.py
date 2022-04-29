from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from students.models import Major, Plan, Teaching, Course
from students.serializers import MajorSerializer, MajorDetailSerializer, PlanSerializer, PlanDetailSerializer, \
    TeachingSerializer, TeachingDetailSerializer, CourseSerializer, CourseDetailSerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all().order_by('-create_time')
    serializer_class = MajorSerializer

    def get_queryset(self):
        queryset = Major.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return MajorSerializer
        else:
            return MajorDetailSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all().order_by('-create_time')
    serializer_class = PlanSerializer

    def get_queryset(self):
        queryset = Plan.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PlanSerializer
        else:
            return PlanDetailSerializer


class TeachingViewSet(viewsets.ModelViewSet):
    queryset = Teaching.objects.all().order_by('-create_time')
    serializer_class = TeachingSerializer

    def get_queryset(self):
        queryset = Teaching.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TeachingSerializer
        else:
            return TeachingDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-create_time')
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSerializer
        else:
            return CourseDetailSerializer
