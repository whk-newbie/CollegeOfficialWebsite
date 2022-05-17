"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from Group.views import GroupNewsViewSet, GroupViewSet, PartyViewSet, HonorViewSet, ManagementViewSet
from MSboard.views import BoardViewSet
from News.views import NewsViewSet
from Thematic.views import InfosViewSet, FilelearnViewSet, ReportViewSet
from information.views import InformationViewSet
from django.conf import settings
from django.conf.urls.static import static

from party.views import PartyBuildingViewSet, PartyFileAndTrendsViewSet
from research.views import ResearchViewSet, InstitutionsViewSet, AchievementsViewSet
from students.views import MajorViewSet, PlanViewSet, TeachingViewSet, CourseViewSet, NoticeViewSet, \
    EnrollmentViewSet, EmploymentViewSet, LearningViewSet
from teachers.views import TeacherViewSet, TeacherMoralityViewSet, RecruitingViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'infos', InformationViewSet)
# 教师模块api
router.register(r'teachers/teacher', TeacherViewSet)
router.register(r'teachers/Tmorality', TeacherMoralityViewSet)
router.register(r'teachers/recruiting', RecruitingViewSet)
# 学生模块api
router.register(r'student/major', MajorViewSet)
router.register(r'student/plan', PlanViewSet)
router.register(r'student/teaching', TeachingViewSet)
router.register(r'student/course', CourseViewSet)
router.register(r'student/notice', NoticeViewSet)
router.register(r'student/enrollment', EnrollmentViewSet)
router.register(r'student/employment', EmploymentViewSet)
router.register(r"student/Learning", LearningViewSet)
# 科学研究模块api
router.register(r'research/research', ResearchViewSet)
router.register(r'research/institutions', InstitutionsViewSet)
router.register(r'research/achievements', AchievementsViewSet)

# 党建党史模块api
router.register(r'party/building', PartyBuildingViewSet)
router.register(r'party/fileandtrends', PartyFileAndTrendsViewSet)

# 团学模块api
router.register(r'group/groupnews', GroupNewsViewSet)
router.register(r'group/group', GroupViewSet)
router.register(r'group/party', PartyViewSet)
router.register(r'group/manage', ManagementViewSet)
router.register(r'group/honor', HonorViewSet)

# 主题教育模块api
router.register(r'education/report', ReportViewSet)
router.register(r'education/infor', InfosViewSet)
router.register(r'education/filelearn', FilelearnViewSet)

router.register(r'board', BoardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'mdeditor/', include('mdeditor.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
