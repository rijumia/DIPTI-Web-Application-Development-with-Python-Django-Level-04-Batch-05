from django.urls import path, include
from employer_app.views import*

urlpatterns = [
    path('employerProfile/',employerProfile, name='employerProfile'),
    path('createJobPage/',createJobPage, name='createJobPage'),

]
