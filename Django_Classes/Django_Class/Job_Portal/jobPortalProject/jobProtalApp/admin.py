from django.contrib import admin
from jobProtalApp.models import CustomUserModel, JobModel
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    list_display =['username','fullName','user_type']
    
admin.site.register(CustomUserModel, CustomAdmin)
admin.site.register(JobModel)
