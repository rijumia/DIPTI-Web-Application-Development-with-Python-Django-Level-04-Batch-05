
from django.contrib import admin
from django.urls import path
from studentApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('addStudent/', addStudent, name='addStudent'),
    path('editStudent/<str:id>', editStudent, name='editStudent'),
    path('viewStudent/<str:id>', viewStudent, name='viewStudent'),
    path('deleteStudent/<str:id>', deleteStudent, name='deleteStudent'),

    
    path('', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('passwordNotMatched/', passwordNotMatched, name='passwordNotMatched'),
    path('passwordWrong/', passwordWrong, name='passwordWrong'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
