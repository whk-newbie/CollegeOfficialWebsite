from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsList.as_view(), name='list'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='detail'),
]