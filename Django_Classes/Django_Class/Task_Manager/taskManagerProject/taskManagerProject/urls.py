from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from taskManagerApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Homepage/', homePage, name='homePage'),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    
    path('addTask/',addTask, name='addTask'),
    path('updateTask/<str:id>/',updateTask, name='updateTask'),
    path('listTask/',listTask, name='listTask'),
    path('deleteTask/<str:id>/',DeleteTask,name='DeleteTask'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
