from django.contrib import admin
from JobNestApp.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(CreateJobModel)
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)
admin.site.register(JobApplication)