from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_types = models.TextField(choices=[
        ('Admin','Admin'),
        ('Teacher','Teacher'),
        ('Student','Student'),
    ],max_length=10, null=True)
    def __str__(self):
        return self.username
    
class ClassModel(models.Model):
    className = models.CharField(max_length=100, null=True)
    seats = models.IntegerField(null=True)

class TeacherModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,related_name='teacher_info', null=True)
    name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=150, null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=15, null=True)

class StudentModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,related_name='student_info', null=True)
    classNam = models.OneToOneField(ClassModel, on_delete=models.CASCADE, related_name='student_class', null=True)
    name = models.CharField(max_length=150, null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=15, null=True)
