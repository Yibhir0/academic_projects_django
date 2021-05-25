"""academic_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# These are the main urls of the webpage. An empty path corresponds to the item app's
# urls which contains urls for the Home, About and Projects tabs. If user_app is entered in the url,
# the user can register, login or view their profile. If the user enters message_app in the url,
# they can view their current messages or look at a specific message.
# (Note: there are no empty url paths in user_app and message_app).
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item_app.urls')),
    path('user_app/', include('user_app.urls')),
    path('message_app/', include('message_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
