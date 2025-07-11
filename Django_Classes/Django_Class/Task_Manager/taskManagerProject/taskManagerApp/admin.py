from django.contrib import admin
from taskManagerApp.models import CustomUserModel, TaskModel
from django.contrib.auth.admin import UserAdmin

class userModel(UserAdmin):
    list_display = [
        'username',
        'fullname',
        'email',   
    ]
    
admin.site.register(CustomUserModel, userModel)
admin.site.register(TaskModel)

