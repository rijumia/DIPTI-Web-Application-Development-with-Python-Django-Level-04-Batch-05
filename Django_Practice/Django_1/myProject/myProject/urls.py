from django.contrib import admin
from django.urls import path
from myProject.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage, name='homePage'),
    path('contact', contactPage, name='contactPage'),
    path('work', workPage, name='workPage'),
    path('about', aboutPage, name='aboutPage'),
    path('login', loginPage, name='loginPage'),
    path('signup', signupPage, name='signupPage'),
    path('viewStudent', viewStudentPage),
    path('viewCourse', coursePage),
]
