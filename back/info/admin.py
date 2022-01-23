from django.contrib import admin

# Register your models here.
from info.models import Infos

admin.site.site_header = '管理平台'
admin.site.site_title = '计算机信息工程学院后台数据管理'
admin.site.register(Infos)
