"""
URL configuration for studentProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentProject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage , name='homePage'),
    path('student/', studentPage , name='studentPage'),
    path('student/studentlist/', studentListPage, name='studentListPage'),
    path('teacher/', teacherPage , name='teacherPage'),
    path('teacher/teacherlist/', teacherListPage , name='teacherListPage'),
    path('course/', coursePage , name='coursePage'),
    path('course/courselist/', courseListPage , name='courseListPage'),
    
    path('student/studentlist/<str:myid>', deleteStudent, name='deleteStudent'),
    path('teacher/teacherlist/<str:myid>', deleteTeacher, name='deleteTeacher'),
    path('course/courselist/<str:myid>', deleteCourse, name='deleteCourse'),
    
    path('student/studentlist/<str:myid>/', editStudent, name='editStudent'),
    path('teacher/teacherlist/<str:myid>/', editTeacher, name='editTeacher'),
    path('course/courselist/<str:myid>/', editCourse, name='editCourse'),
]
