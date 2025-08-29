from django.urls import path 
from .views import *

urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('logout/', logoutPage, name='logoutPage'),
    path('register/', registerPage, name='registerPage'),

    path('dashboard/', dashboard, name='dashboard'),
]
