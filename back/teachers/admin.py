from django.contrib import admin

# Register your models here.
"""
Teachers/admin.py
"""
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_title', 'updated')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'job_title')
    search_fields = ('name',)  # 'job_title'
    list_per_page = 25
    ordering = ('id',)


