from django.contrib import admin
from to_do_App.models import CustomUserModel, ToDoModel
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ['username','email','city_name']

admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(ToDoModel)

