from django.contrib import admin
from schoolApp.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(ClassModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)