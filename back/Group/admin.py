from django.contrib import admin

# Register your models here.

# Base admin class
from Group.models import News, Group, Party, System, Honor


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time', 'update_time')
    list_display_links = ('id', 'title')
    list_filter = ('create_time',)
    search_fields = ('title',)
    list_per_page = 50


@admin.register(News)
class NewsAdmin(BaseAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseAdmin):
    pass


@admin.register(Party)
class PartyAdmin(BaseAdmin):
    pass


@admin.register(System)
class SystemAdmin(BaseAdmin):
    pass


@admin.register(Honor)
class HonorAdmin(BaseAdmin):
    pass
