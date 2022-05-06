from django.contrib import admin

# Register your models here.
from research.models import Research, institutions, achievements


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'create_time')
    list_per_page = 25
    list_filter = ('create_time',)
    date_hierarchy = 'create_time'
    ordering = ('-create_time',)


@admin.register(institutions)
class InstitutionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'create_time')
    list_per_page = 25
    list_filter = ('create_time',)
    date_hierarchy = 'create_time'
    ordering = ('-create_time',)


@admin.register(achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'create_time')
    list_per_page = 25
    list_filter = ('create_time',)
    date_hierarchy = 'create_time'
    ordering = ('-create_time',)
