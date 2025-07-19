from django.urls import path, include
from users_auth_app.views import *

urlpatterns = [
    path('',signupPage, name='signupPage'),
    path('login/',loginPage, name='loginPage'),
    path('changePasswordPage/',changePasswordPage, name='changePasswordPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    
    
    path('dashboard/',dashboardPage, name='dashboardPage'),
    path('profile/',profilePage, name='profilePage'),
    path('profileUpdatePage/',profileUpdatePage, name='profileUpdatePage'),
    path('pendingList/',pendingList, name='pendingList'),
    
    path('approve/<str:id>/', approveUser, name='approveUser'),
    path('reject/<str:id>/', rejectUser, name='rejectUser'),

]