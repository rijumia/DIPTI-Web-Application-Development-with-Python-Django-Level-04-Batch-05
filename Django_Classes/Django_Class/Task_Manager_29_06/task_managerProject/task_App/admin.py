from django.contrib import admin
from task_App.models import CustomUserModel, TaskModel

admin.site.register(CustomUserModel)
admin.site.register(TaskModel)
