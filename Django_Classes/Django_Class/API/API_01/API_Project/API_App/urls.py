from django.urls import path
from API_App.views import *


urlpatterns = [
    path('student-list/', studentList, name='studentList'),
]
