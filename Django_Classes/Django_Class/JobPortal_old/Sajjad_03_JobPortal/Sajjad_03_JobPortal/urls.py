from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    
    # job
    path('addjob/',addjob,name='addjob'),
    path('joblist/',joblist,name='joblist'),
    path('deletejob/<str:jobid>',deletejob,name='deletejob'),
    path('editjob/<str:jobid>',editjob,name='editjob'),
    path('applyjob/<str:jobid>',applyjob,name='applyjob'),
    
    # profile 
    path('baseprofile/',baseprofile,name='baseprofile'),
    path('basicinfo/',basicinfo,name='basicinfo'),
    path('editbasic/<str:basicid>',editbasic,name='editbasic'),
    path('editseekerotherinfo/<str:seekerid>',editseekerotherinfo,name='editseekerotherinfo'),
    
    # seeker 
    path('seekerotherinfo/',seekerotherinfo,name='seekerotherinfo'),
    path('appliedjob/',appliedjob,name='appliedjob'),
    
    # recruiter 
    path('recruiterotherinfo/',recruiterotherinfo,name='recruiterotherinfo'),
    path('postedjob/',postedjob,name='postedjob'),

    # search

    path('searchpage/',searchpage,name='searchpage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
