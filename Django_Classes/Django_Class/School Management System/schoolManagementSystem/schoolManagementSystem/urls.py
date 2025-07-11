from django.contrib import admin
from django.urls import path
from schoolManagementApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
    path('profilePage/', profilePage, name='profilePage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('homePage/', homePage, name='homePage'),
    path('addStudent/', addStudent, name='addStudent'),
    path('studentList/', studentList, name='studentList'),
]
