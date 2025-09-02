from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base, name='base'),
     # Company URLs
    path('company/', company_list, name='company_list'),
    path('company/create/', company_create, name='company_create'),
    path('company/<int:pk>/edit/', company_update, name='company_edit'),
    path('company/<int:pk>/delete/', company_delete, name='company_delete'),

    # Employee URLs
    path('employee/', employee_list, name='employee_list'),
    path('employee/create/', employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', employee_update, name='employee_edit'),
    path('employee/<int:pk>/delete/', employee_delete, name='employee_delete'),

    # Product URLs
    path('product/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_update, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),

    # Job URLs
    path('job/', job_list, name='job_list'),
    path('job/create/', job_create, name='job_create'),
    path('job/<int:pk>/edit/', job_update, name='job_edit'),
    path('job/<int:pk>/delete/', job_delete, name='job_delete'),
]
