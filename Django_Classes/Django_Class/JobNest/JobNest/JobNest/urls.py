from django.contrib import admin
from django.urls import path
from JobNestApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signupPage, name='signupPage'),
    path('log-in/',loginPage, name='loginPage'),
    path('changePassword/',changePassword, name='changePassword'),
    path('log-out/',logoutPage, name='logoutPage'),
    
    path('dashboardPage/', dashboardPage, name='dashboardPage'),
    path('profilePage/', profilePage, name='profilePage'),
    
    path('createJobPage/', createJobPage, name='createJobPage'),
    path('jobListPage/', jobListPage, name='jobListPage'),
]
