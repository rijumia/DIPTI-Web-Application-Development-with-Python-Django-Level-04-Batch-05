from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    email = models.EmailField(null=True)
    
class StudentModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=50, null=True)
    studentId = models.PositiveIntegerField(null=True)
    
class ProjectModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100, null=True)
    project_description = models.TextField(null=True)
    project_status = models.CharField(choices=[
        ('NotStarted','NotStarted'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ],max_length=15, null=True)
    deadline = models.DateField(null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    