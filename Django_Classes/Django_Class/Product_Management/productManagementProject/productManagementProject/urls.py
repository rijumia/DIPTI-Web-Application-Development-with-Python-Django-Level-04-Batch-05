from django.contrib import admin
from django.urls import path
from productManagementProject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homePage, name = 'homePage'),
    path('product/', productPage, name = 'productPage'),
    path('addProduct/', addProductPage, name = 'addProductPage'),
]
