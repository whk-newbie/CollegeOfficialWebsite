from django.contrib import admin

# Register your models here.
from research.models import Research, institutions, achievements


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'date')
    list_per_page = 25
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)


@admin.register(institutions)
class InstitutionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'date')
    list_per_page = 25
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)


@admin.register(achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'date')
    list_per_page = 25
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)
