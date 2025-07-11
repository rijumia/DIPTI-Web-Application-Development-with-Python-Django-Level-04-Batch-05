from django.urls import path
from UserAuthApp.views import *

urlpatterns = [
    path('',registerPage, name='registerPage'),
    path('loginPage/',loginPage, name='loginPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('changePasswordPage/',changePasswordPage, name='changePasswordPage'),
    path('profileInfoPage/',profileInfoPage, name='profileInfoPage'),

    path('homePage/',homePage, name='homePage'),
]