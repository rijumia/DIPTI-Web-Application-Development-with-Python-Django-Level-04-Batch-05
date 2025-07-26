from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from OMS_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/', signupPage, name='signupPage'),
    path('', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('dashboard/', dashboardPage, name='dashboardPage'),

    path('add-employee/', addEmployeePage, name='addEmployeePage'),
    path('employeePage/', employeePage, name='employeePage'),
    
    path('add-department/', addDepartmentPage, name='addDepartmentPage'),
    path('department-list/', departmentPage, name='departmentPage'),
    
    path('leaveRequest-list/', leaveRequestPage, name='leaveRequestPage'),
    path('Leave-Approve/<str:id>/', ApprovePage, name='ApprovePage'),
    path('Leave-Rehect/<str:id>/', RejectedPage, name='RejectedPage'),
    #Employee
    path('addLeavePage/', addLeavePage, name='addLeavePage'),
    path('leaveList/', leaveListPage, name='leaveListPage'),
    path('profilePage/', profilePage, name='profilePage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
