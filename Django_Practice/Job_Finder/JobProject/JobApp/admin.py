from django.contrib import admin
from JobApp.models import CustomUserModel, JobModel

admin.site.register(CustomUserModel)
admin.site.register(JobModel)
