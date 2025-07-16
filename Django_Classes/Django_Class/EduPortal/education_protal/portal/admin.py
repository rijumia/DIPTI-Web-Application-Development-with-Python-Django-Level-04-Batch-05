from django.contrib import admin
from portal.models import*

admin.site.register(CustomUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentBasicInfoModel)
admin.site.register(StudentEducationInfoModel)
