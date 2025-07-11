from django.contrib import admin
from UserAuthApp.models import*

admin.site.register(CustomUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)