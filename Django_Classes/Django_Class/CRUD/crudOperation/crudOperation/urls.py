from django.contrib import admin
from django.urls import path
from crudOperation.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('add/', addPage, name='addPage'),
    path('add/list/', listPage, name='listPage'),
    
    path('delete/<str:myid>/', deletePage, name="deletePage"),
    
    path('update/<str:myid>/', updatePage, name="updatePage"),
]
