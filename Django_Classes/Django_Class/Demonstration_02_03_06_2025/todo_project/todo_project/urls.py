from django.contrib import admin
from django.urls import path
from todo_project.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('addtask/', addPage, name='addPage'),
    path('addtask/tasklist/', listPage, name='listPage'),
    path('addtask/tasklist/<str:id>/', deleteTaskPage, name='deleteTaskPage'),
    path('addtask/tasklist/update/<str:id>/', updateTaskPage, name='updateTaskPage'),
    path('viewtask/<str:id>/', viewPage, name='viewPage'),
]
