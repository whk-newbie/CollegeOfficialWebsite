from django.contrib import admin

# Register your models here.
from party.models import PartyBuilding, PartyFileAndTrends


@admin.register(PartyBuilding)
class PartyBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_time')
    list_display_links = ('id', 'title')
    list_filter = ('create_time',)
    search_fields = ('title', 'content')
    list_per_page = 50
    ordering = ('-create_time',)


@admin.register(PartyFileAndTrends)
class PartyFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time')
    list_display_links = ('id', 'title')
    list_filter = ('create_time',)
    search_fields = ('title', 'category')
    list_per_page = 50

