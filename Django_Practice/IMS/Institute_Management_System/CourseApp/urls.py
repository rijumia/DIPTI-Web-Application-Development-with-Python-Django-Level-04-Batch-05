from django.urls import path
from .views import createCoursePage, coursePage


urlpatterns = [
    path('createCoursePage/', createCoursePage, name='createCoursePage'),
    path('coursePage/', coursePage, name='coursePage'),
]