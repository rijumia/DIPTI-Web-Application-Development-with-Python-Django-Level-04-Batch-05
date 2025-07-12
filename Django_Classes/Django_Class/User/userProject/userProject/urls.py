from django.contrib import admin
from django.urls import path
from userProject.views import homePage, addUserPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('add-user/', addUserPage, name='addUserPage'),
]
