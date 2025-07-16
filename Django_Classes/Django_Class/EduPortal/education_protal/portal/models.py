from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[
        ('Admin','Admi'),
        ('Teacher', 'Teacher'),
    ],max_length=20, null=True)
    
class TeacherModel(models.Model):
    teacherName = models.CharField(max_length=50, null=True)
    lastEducation = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    
class StudentBasicInfoModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    
class StudentEducationInfoModel(models.Model):
    student = models.ForeignKey(StudentBasicInfoModel,on_delete=models.CASCADE, null=True)
    degreeName = models.CharField(max_length=20, null=True)
    grade = models.CharField(max_length=20, null=True)
    passingYear = models.PositiveIntegerField(null=True)