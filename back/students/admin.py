from django.contrib import admin


# Register your models here.
from students.models import Major


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_time',)
    list_display_links = ('id', 'name', 'category',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('-create_time',)

