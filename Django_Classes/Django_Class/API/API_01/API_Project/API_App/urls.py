from django.urls import path
from API_App.views import *


urlpatterns = [
    path('student-list/', studentList, name='studentList'),
    path('add-student/', addStudent, name='addStudent'),
    path('update-student/<int:pk>/', updateStudent, name='updateStudent'),
    path('delete-student/<int:pk>/', deleteStudent, name='deleteStudent'),
]
