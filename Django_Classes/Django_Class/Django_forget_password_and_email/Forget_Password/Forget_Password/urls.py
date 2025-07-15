from django.contrib import admin
from django.urls import path
from ForgetApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sendMailPage, name='sendMailPage'),
]
