from django.contrib import admin

# Register your models here.
from party.models import PartyBuilding, PartyFileAndTrends


@admin.register(PartyBuilding)
class PartyBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'time')
    list_display_links = ('id', 'title')
    list_filter = ('time',)
    search_fields = ('title', 'content')
    list_per_page = 50
    ordering = ('-time',)


@admin.register(PartyFileAndTrends)
class PartyFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'time')
    list_display_links = ('id', 'title')
    list_filter = ('time',)
    search_fields = ('title', 'category')
    list_per_page = 50
