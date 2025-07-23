from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_types = models.CharField(choices=[
        ('Recruiter','Recruiter'),
        ('Job_seeker','Job_seeker'),
    ],max_length=15, null=True)
    phone = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.username
    
class CreateJobModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='user_info' ,null=True)
    JobTitle = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    salary = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=50, null=True)
    deadline = models.DateField(null=True)
    post_at = models.DateTimeField(auto_now_add=True,null=True)

    
