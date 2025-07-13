from django.contrib import admin
from userAuth.models import *

# Register your models here.


# From userAuth model
admin.site.register(CustomUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
admin.site.register(PendingStudentModel)