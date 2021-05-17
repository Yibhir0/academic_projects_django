from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('user_register/', views.register, name='user-register'),
    path('user_login/', LoginView.as_view(template_name = 'user_app/login.html'), name ='user-login'),
    path('user_logout/', LogoutView.as_view(template_name = 'user_app/logout.html'), name ='user-logout'),
]