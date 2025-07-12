from django.contrib import admin
from schoolManagementApp.models import CustomUserModel, TeacherModel, StudentModel

admin.site.register(CustomUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
