from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from project.models import *

class CustomAdmin(UserAdmin):
    list_display = ['username','email']
    
admin.site.register(CustomUserModel,CustomAdmin)
admin.site.register(StudentModel)
admin.site.register(ProjectModel)
