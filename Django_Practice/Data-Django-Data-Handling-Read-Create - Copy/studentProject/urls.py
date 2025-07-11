from django.contrib import admin
from django.urls import path
from studentProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name = 'homePage'),
    path('studentlist/', studentListPage, name = 'studentListPage'),
    path('addstudent/', addStudentPage, name = 'addStudentPage'),
]
