from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from students.models import Major, Plan, Teaching, Course, Notice, Enrollment, Employment, Learning
from students.serializers import MajorSerializer, MajorDetailSerializer, PlanSerializer, PlanDetailSerializer, \
    TeachingSerializer, TeachingDetailSerializer, CourseSerializer, CourseDetailSerializer, NoticeSerializer, \
    NoticeDetailSerializer, EnrollmentSerializer, EnrollmentDetailSerializer, EmploymentSerializer, \
    EmploymentDetailSerializer, LearningSerializer


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


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-create_time')
    serializer_class = NoticeSerializer

    def get_queryset(self):
        queryset = Notice.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return NoticeSerializer
        else:
            return NoticeDetailSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all().order_by('-create_time')
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EnrollmentSerializer
        else:
            return EnrollmentDetailSerializer


class EmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.all().order_by('-create_time')
    serializer_class = EmploymentSerializer

    def get_queryset(self):
        queryset = Employment.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EmploymentSerializer
        else:
            return EmploymentDetailSerializer

class LearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all().order_by('-create_time')
    serializer_class = LearningSerializer

    def get_queryset(self):
        queryset = Learning.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

