from django.contrib import admin

# Register your models here.
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'degree')
    list_display_links = ('name', 'job_title', 'degree')
    list_filter = ('job_title', 'degree')
    search_fields = ('name', 'job_title', 'degree')
    list_per_page = 25
    ordering = ['name']
