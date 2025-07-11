from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from studentApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
    path('logout/', logoutPage, name='logoutPage'),
    
    path('homePage/',homePage, name='homePage'),
    
    path('addStudent/', addStudent, name='addStudent'),
    path('studentUpdate/<str:id>/', studentUpdate, name='studentUpdate'),
    path('studentList/', studentList, name='studentList'),
    path('studentDelete/<str:id>/',studentDelete, name='studentDelete'),
    path('studentView/<str:id>/',studentView, name='studentView'),
    
    
    path('addTask/', addTask, name='addTask'),
    path('tasktUpdate/<str:id>/', taskUpdate, name='taskUpdate'),
    # path('studentList/', studentList, name='studentList'),
    path('taskDelete/<str:id>/',taskDelete, name='taskDelete'),
    # path('studentView/<str:id>/',studentView, name='studentView'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
