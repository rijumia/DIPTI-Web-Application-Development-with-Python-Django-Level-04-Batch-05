from django.contrib import admin
from django.urls import path
from CRUDapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('companyList/', companyList, name='companyList'),
    path('addCompany/', addCompany, name='addCompany'),
    path('updateCompany/<str:id>/', updateCompany, name='updateCompany'),
    path('deleteCompany/<str:id>/', deleteCompany, name='deleteCompany'),

    path('addEmployee/', addEmployee, name='addEmployee'),
    path('employeeList/', employeeList, name='employeeList'),
    path('updateEmployee/<str:id>/', updateEmployee, name='updateEmployee'),
    path('deleteEmployee/<str:id>/', deleteEmployee, name='deleteEmployee'),

    path('addProduct/', addProduct, name='addProduct'),
    path('productList/', productList, name='productList'),
    path('updateProduct/<str:id>/', updateProduct, name='updateProduct'),
    path('deleteProduct/<str:id>/', deleteProduct, name='deleteProduct'),

    path('addJob/', addJob, name='addJob'),
    path('jobList/', jobList, name='jobList'),
    path('updateJob/<str:id>/', updateJob, name='updateJob'),
    path('deleteJob/<str:id>/', deleteJob, name='deleteJob'),
]
