from django.urls import path
from courses.views import *

urlpatterns = [
    # ----------Authenticate urls---------------
    path('addCourse/', addCourse, name='addCourse'),
    path('course/', course, name='course'),
]