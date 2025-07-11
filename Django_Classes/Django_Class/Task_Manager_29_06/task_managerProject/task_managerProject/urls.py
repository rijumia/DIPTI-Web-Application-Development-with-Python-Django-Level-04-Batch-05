from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('homePage/', homePage, name='homePage'),
    path('addTask/',addTask,name='addTask'),
    path('listTask/',listTask, name='listTask'),
    path('updateTask/<str:id>/', updateTask, name='updateTask'),
    path('deleteTask/<str:id>/', deleteTask, name='DeleteTask'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
    
    path('taskDone/<str:id>/', taskDone, name='taskDone'),
    path('changeStatus/<str:id>/', changeStatus, name='changeStatus'),
    path('changePriority/<str:id>/', changePriority, name='changePriority'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
