from django.urls import path
from UserAuthApp.views import *

urlpatterns = [
    path('',registerPage, name='registerPage'),
    path('loginPage/',loginPage, name='loginPage'),
]