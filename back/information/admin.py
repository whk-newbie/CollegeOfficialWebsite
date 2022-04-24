from django.contrib import admin

# Register your models here.
from information.models import Information


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_time')
    list_display_links = ('id', 'title', 'pub_time')
    list_filter = ('pub_time',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ("id",)

    fieldsets = (
        ('', {'fields': (('pub_time', 'author'),)}),
        ('', {'fields': (('file',),)}),
        ('', {'fields': (('title',),)}),
        ('', {'fields': (('content',),)}),
    )
