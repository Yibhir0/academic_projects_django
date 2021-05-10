from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_list/',views.ProjectListView.as_view(),name='project-list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
