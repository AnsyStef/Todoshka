from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
import django
from . import settings


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

handler404 = "main.views.pageNotFound"