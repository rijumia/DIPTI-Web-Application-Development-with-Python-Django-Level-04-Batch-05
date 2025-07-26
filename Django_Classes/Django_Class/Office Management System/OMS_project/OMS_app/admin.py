from django.contrib import admin
from OMS_app.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(DepartmentModel)
admin.site.register(EmployeeManagementModel)
admin.site.register(LeaveModel)