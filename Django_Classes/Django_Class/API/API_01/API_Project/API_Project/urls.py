from django.contrib import admin
from django.urls import path, include
from API_App.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API_App.urls')),
]
