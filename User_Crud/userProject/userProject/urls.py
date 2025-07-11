from django.contrib import admin
from django.urls import path
from userProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('add/', addPage, name='addPage'),
    path('list/', listPage, name='listPage'),
    path('list/<str:id>/', deletePage, name='deletePage'),
    path('edit/<str:id>/', editPage, name='editPage'),
    path('view/<str:id>', viewPage, name='viewPage'),
]
