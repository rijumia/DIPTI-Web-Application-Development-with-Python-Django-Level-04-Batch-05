from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[
        ('Admin','Admin'),
        ('Teacher', 'Teacher'),
    ],max_length=10, null=True)

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    hire_date = models.DateField(null=True)

class StudentModel(models.Model):
    teacher = models.ForeignKey(TeacherModel,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    age = models.PositiveIntegerField(null=True)  
    grade = models.CharField(max_length=15,null=True)
    enrollment_date = models.DateField(auto_now_add=True,null=True)
    
    
