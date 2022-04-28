from django.contrib import admin

# Register your models here.

from News.models import News


# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    admin.site.site_title = "计算机信息工程学院"
    admin.site.site_header = "学院后台管理"

    # list_display = 你需要展示的字段应该写在这里,此处是数据库中的字段
    list_display = ("id", "title", "body", "create_time", "update_time")
    # list_display = 点击字段可以编辑
    list_display_links = ('id', 'title', 'body', "create_time", "update_time")
    # search_fields = 用于添加一个搜索框,此处以title作为查询条件
    search_fields = ("title",)
    # list_filter = 设置一个过滤器,此处是以hostname作为过滤条件
    list_filter = ("create_time", "update_time")
    # ordering = 设置一个排序条件,此处是以id作为排序依据
    ordering = ("id",)
    # list_per_page = 设置每页显示多少条记录,默认是100条
    list_per_page = 10
    # list_editable = 设置默认可编辑字段
    # list_editable = ("title", "body", "create_time")
    # date_hierarchy = 显示详细时间分层筛选
    date_hierarchy = 'create_time'
    # readonly_fields = 可以设置只读字段,就是无法修改的字段
    # readonly_fields = ()

    fieldsets = (
        ('', {'fields': (('create_time', 'author'),)}),
        ('', {'fields': (('cover',),)}),
        ('', {'fields': (('title',),)}),
        ('', {'fields': (('body',),)}),
    )



