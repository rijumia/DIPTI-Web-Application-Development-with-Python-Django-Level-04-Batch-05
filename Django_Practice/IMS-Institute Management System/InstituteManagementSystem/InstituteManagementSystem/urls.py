from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AuthUserApp.urls')),
    path('course/',include('Course_App.urls')),
]
