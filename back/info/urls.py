from django.urls import path
from info import views

app_name = 'info'

urlpatterns = [
    path('', views.InfoList.as_view(), name='infolist'),
    path('<int:pk>/', views.InfoDetail.as_view(), name='detail'),
]
