from django.contrib import admin

# Register your models here.
# Base admin class
from Thematic.models import report, infos, filelearn


class BaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_time']
    list_display_links = ['id', 'title']
    list_filter = ['create_time']
    search_fields = ['title']
    list_per_page = 10


@admin.register(report)
class ReportAdmin(BaseAdmin):
    pass


@admin.register(infos)
class InfosAdmin(BaseAdmin):
    pass


@admin.register(filelearn)
class FileLearnAdmin(BaseAdmin):
    pass
