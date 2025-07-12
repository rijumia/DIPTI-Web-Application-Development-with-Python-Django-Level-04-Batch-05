from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ], max_length=10, null=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', null=True, blank=True)

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    contact_number = models.CharField(max_length=15, null=True)
    designation = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.designation}"
    
class StudentModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    contact_number = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.department}"