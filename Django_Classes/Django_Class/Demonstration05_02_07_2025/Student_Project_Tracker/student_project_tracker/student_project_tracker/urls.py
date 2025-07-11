"""
URL configuration for student_project_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    
    path('homePage/', homePage, name='homePage'),
    path('addPage/', addPage, name='addPage'),
    path('updatePage/<str:id>/', updatePage, name='updatePage'),
    path('listPage/', listPage, name='listPage'),
    path('deletePage/<str:id>/', deletePage, name='deletePage'),
    path('viewPage/<str:id>/', viewPage, name='viewPage'),
    
    path('changeStatus/<str:id>/',changeStatus, name='changeStatus'),
]
