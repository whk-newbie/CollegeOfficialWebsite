from django.contrib import admin

# Register your models here.
from students.models import Major, Plan, Teaching, Course


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_time',)
    list_display_links = ('id', 'name', 'category',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_time',)
    list_display_links = ('id', 'name', 'category',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_time',)
    list_display_links = ('id', 'name', 'category',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('-create_time',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_time',)
    list_display_links = ('id', 'name', 'category',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('-create_time',)
