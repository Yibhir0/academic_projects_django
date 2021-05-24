# Yassine Ibhir
# urls for user_app
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,PasswordResetConfirmView )

from . import views


urlpatterns = [
    path('user_register/', views.register, name='user-register'),
    path('user_login/', views.UserLoginView.as_view(), name ='user-login'),
    path('user_logout/', views.UserLogoutView.as_view(), name ='user-logout'),
    path('user_profile/', views.viewProfile, name ='user-profile'),
    path('user_update/', views.updateProfile, name ='user-update'),
    path('password_reset/', PasswordResetView.as_view(template_name='user_app/password_reset.html'), name='password_reset'),
    path('password_reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]