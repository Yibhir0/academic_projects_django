from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_login/', views.MemberLoginListView.as_view(), name='admin-login'),
]