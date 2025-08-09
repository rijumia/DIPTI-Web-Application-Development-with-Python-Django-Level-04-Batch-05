from django.contrib import admin
from django.urls import path
from schoolApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage, name='signupPage'),
    path('log-in/', loginPage, name='loginPage'),
    path('log-out/', logoutPage, name='logoutPage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),

    path('add-teacher/', addTeacher, name='addTeacher'),
    path('teacher-list/', teacherList, name='teacherList'),
]
