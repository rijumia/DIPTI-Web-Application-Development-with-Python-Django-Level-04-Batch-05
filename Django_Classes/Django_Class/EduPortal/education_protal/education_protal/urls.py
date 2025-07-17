from django.contrib import admin
from django.urls import path
from portal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('verifyOtp/', verifyOtp, name='verifyOtp'),
    
    path('dashboardPage/', dashboardPage, name='dashboardPage'),
    
    path('addTeacherPage/', addTeacherPage, name='addTeacherPage'),
    path('updateTeacherPage/<str:id>', updateTeacherPage, name='updateTeacherPage'),
    path('allTeacherPage/', allTeacherPage, name='allTeacherPage'),
    
    path('addStudentPage/', addStudentPage, name='addStudentPage'),
    path('studentList/', studentList, name='studentList'),
]
