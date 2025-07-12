from django.urls import path
from CourseApp.views import *

urlpatterns = [
    path('createCoursePage/',createCoursePage, name='createCoursePage'),
]
