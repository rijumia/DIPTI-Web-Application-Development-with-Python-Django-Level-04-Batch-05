from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from instituteApp.models import CustomUserModel, TeacherModel, StudentModel


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type')

admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)