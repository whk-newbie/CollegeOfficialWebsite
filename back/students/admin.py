from django.contrib import admin

# Register your models here.
from students.models import Major, Plan, Teaching, Course, Notice, Enrollment, Employment, Learning


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time',)
    list_display_links = ('id', 'title', 'category',)
    list_filter = ('category',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time',)
    list_display_links = ('id', 'title', 'category',)
    list_filter = ('category',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time',)
    list_display_links = ('id', 'title', 'category',)
    list_filter = ('category',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time',)
    list_display_links = ('id', 'title', 'category',)
    list_filter = ('category',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time',)
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time',)
    list_display_links = ('id', 'title','category',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category' ,'create_time',)
    list_display_links = ('id', 'title','category',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time',)
    list_display_links = ('id', 'title', 'category',)
    list_filter = ('category',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('-create_time',)
