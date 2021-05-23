from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_list/',views.ProjectListView.as_view(),name='project-list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('search_list/', views.searchProjectKeyWord.as_view(), name='search-list'),
    path('memberSearch_list/', views.searchMemberProjectKeyWord.as_view(), name='memberSearch-list'),
    path('memberProject_list/', views.ProjectMemberListView.as_view(), name='memberProject-list'),
    path('project/add/', views.ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
]
