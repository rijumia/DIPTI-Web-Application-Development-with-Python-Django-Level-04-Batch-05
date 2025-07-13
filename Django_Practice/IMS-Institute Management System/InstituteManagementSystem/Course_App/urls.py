from django.urls import path
from Course_App.views import*

urlpatterns = [
    path('createCoursePage/',createCoursePage, name='createCoursePage'),
    path('allCoursePage/',allCoursePage, name='allCoursePage'),

    path('admitedCoursePage/',admitedCoursePage, name='admitedCoursePage'),
    path('admittedCourseListPage/',admittedCourseListPage, name='admittedCourseListPage'),
    
]