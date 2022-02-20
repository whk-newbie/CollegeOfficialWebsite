from django.urls import path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('', views.TeachersListView.as_view(), name='list'),
    path('<int:pk>/', views.TeachersDetailView.as_view(), name='detail'),
]