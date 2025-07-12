from django.db import models
from UserAuthApp.models import TeacherModel, StudentModel


class CourseModel(models.Model):
    course_title = models.CharField(max_length=100,null=True)
