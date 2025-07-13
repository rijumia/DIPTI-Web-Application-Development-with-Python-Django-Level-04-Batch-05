from django.contrib import admin
from courses.models import *

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(AdmittedCourseModel)
admin.site.register(PaymentHistoryModel)