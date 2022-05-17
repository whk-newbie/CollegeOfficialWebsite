from django.contrib import admin

# Register your models here.
from anniversary.models import Anniversary


@admin.register(Anniversary)
class AnniversaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_time')
    list_display_links = ('id', 'title')
    list_filter = ('create_time',)
    search_fields = ('title', 'content')
    list_per_page = 50
    ordering = ('-create_time',)
