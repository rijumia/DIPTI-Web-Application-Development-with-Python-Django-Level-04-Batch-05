from django.contrib import admin
from django.urls import path, include
from authApp.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authApp.urls')),
]
