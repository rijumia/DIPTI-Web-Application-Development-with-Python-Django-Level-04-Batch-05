from django.contrib import admin
from django.urls import path
from studentManagementSystemApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('logOutPage/', logOutPage, name='logOutPage'),
    path('homePage/', homePage, name='homePage'),
]
