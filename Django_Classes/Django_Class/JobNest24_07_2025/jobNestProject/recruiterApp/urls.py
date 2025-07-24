from django.urls import path,include
from recruiterApp.views import*

urlpatterns = [
    path('profile/', recruiterProfile, name='recruiterProfile'),
    path('update-profile/', recruiterProfileUpdate, name='recruiterProfileUpdate'),
    path('job-post/', jobPostPage, name='jobPostPage'),
    path('job-list/', jobList, name='jobList'),
]
