from django.contrib import admin
from AuthUserApp.models import*

admin.site.register(CustomUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
admin.site.register(PendingModeel)
