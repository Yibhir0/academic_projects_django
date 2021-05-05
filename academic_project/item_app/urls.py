from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects_list/',views.ProjectListView.as_view(),name='all-projects'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
