from django.contrib import admin
from django.urls import path
from instituteApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerPage, name='registerPage'),
]
