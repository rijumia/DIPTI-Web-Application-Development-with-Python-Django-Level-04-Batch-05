from django.contrib import admin
from django.urls import path
from taskManager.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePge'),
    path('addtask/', addTaskPage, name='addTaskPage'),
    path('addtask/tasklist/', taskListPage, name='taskListPage'),
    path('addtask/tasklist/delete/<str:id>/', deleteTask, name='deleteTask'),
    path('addtask/tasklist/update/<str:id>/', updateTask, name='updateTask'),
    path('addtask/tasklist/detail/<str:id>/', taskDetail, name='taskDetail'),
]
