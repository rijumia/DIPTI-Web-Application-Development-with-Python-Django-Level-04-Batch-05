from django.contrib import admin
from django.urls import path
from studentProject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('addStudent/', addStudentPage, name='addStudentPage'),
    path('studentList/', studentListPage, name='studentListPage'),
    path('deleteStudent/<int:myid>/', deleteStudent, name='deleteStudent'),
    path('updateStudent/<int:myid>/', updateStudent, name='updateStudent'),

    path('addTeacher/', addTeacherPage, name='addTeacherPage'),
    path('addTeacher/teacherList/', teacherListPage, name='teacherListPage'),
    path('deleteTeacher/<int:myid>/', deleteTeacher, name='deleteTeacher'),
    path('updateTeacher/<int:myid>/', updateTeacher, name='updateTeacher'),
]
