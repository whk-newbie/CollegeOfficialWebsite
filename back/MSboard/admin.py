from django.contrib import admin

# Register your models here.
from MSboard.models import board


@admin.register(board)
class boardAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_reply', 'created_at')
    list_filter = ('is_reply',)
    ordering = ('-created_at',)
    list_editable = ('is_reply',)
    # 分页
    list_per_page = 20
