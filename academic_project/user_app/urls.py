from django.urls import path


from . import views

urlpatterns = [
    path('user_register/', views.register, name='user-register'),
    path('user_login/', views.UserLoginView.as_view(), name ='user-login'),
    path('user_logout/', views.UserLogoutView.as_view(), name ='user-logout'),
]