from django.contrib import admin
from CRUDapp.models import *

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(EmployeeModel)
admin.site.register(ProductModel)
admin.site.register(JobModel)