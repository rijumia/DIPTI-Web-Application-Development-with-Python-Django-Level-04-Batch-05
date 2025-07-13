from django.contrib import admin
from Course_App.models import *

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(AdmittedCourseModel)
admin.site.register(PaymentHistoryModel)
