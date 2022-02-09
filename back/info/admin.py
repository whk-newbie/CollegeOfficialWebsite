from django.contrib import admin

# Register your models here.
from info.models import Infos


@admin.register(Infos)
class InfoAdmin(admin.ModelAdmin):
    admin.site.site_title = "计算机信息工程学院"
    admin.site.site_header = "学院后台管理"

    # list_display = 你需要展示的字段应该写在这里,此处是数据库中的字段
    list_display = ("id", "title", "time", "update_time")
    # search_fields = 用于添加一个搜索框,此处以title作为查询条件
    list_display_links = ('id', 'title', 'time', "update_time")
    search_fields = ("title",)
    # list_filter = 设置一个过滤器,此处是以hostname作为过滤条件
    list_filter = ("time","update_time")
    # ordering = 设置一个排序条件,此处是以id作为排序依据
    ordering = ("id",)
    # list_per_page = 设置每页显示多少条记录,默认是100条
    list_per_page = 10
    # list_editable = 设置默认可编辑字段
    # list_editable = ("DataTime",)
    # date_hierarchy = 显示详细时间分层筛选
    date_hierarchy = 'time'
    # readonly_fields = 可以设置只读字段,就是无法修改的字段
    # readonly_fields = ()
