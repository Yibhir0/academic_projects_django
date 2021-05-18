from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_list/',views.ProjectListView.as_view(),name='project-list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('search_list/', views.searchProjectKeyWord.as_view(), name='search-list'),
    path('update_likes/<int:pk>/', views.ProjectDetailView.as_view(), name='update-likes'),
    path('update_rating/<int:pk>/', views.ProjectDetailView.as_view(), name='update-rating'),
    path('user_login/', LoginView.as_view(template_name = 'user_app/login.html'), name ='user-login'),
]
