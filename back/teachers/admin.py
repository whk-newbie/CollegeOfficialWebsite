from django.contrib import admin

# Register your models here.
from .models import Teacher, TeacherMorality, recruiting


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'position', 'degree')
    list_display_links = ('name', 'job_title', 'position', 'degree')
    list_filter = ('job_title', 'degree')
    search_fields = ('name', 'job_title', 'degree')
    list_per_page = 25
    ordering = ['name']


@admin.register(TeacherMorality)
class TeacherMoralityAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')
    list_display_links = ('title', 'content', 'create_time')
    list_filter = ('create_time',)
    search_fields = ('name', 'content')
    list_per_page = 25


@admin.register(recruiting)
class recruitingAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')
    list_display_links = ('title', 'content', 'create_time')
    list_filter = ('create_time',)
    search_fields = ('name', 'content')
    list_per_page = 25
