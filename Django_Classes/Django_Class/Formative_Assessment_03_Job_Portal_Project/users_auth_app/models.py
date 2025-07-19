from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    user_types = models.CharField(choices=[
        ('Admin', 'Admin'),
        ('Employer', 'Employer'),
        ('Candidate', 'Candidate'),
    ],max_length=10,null=True)
    
    
class PendingAccountModel(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    user_types = models.CharField(choices=[
        ('Employer', 'Employer'),
        ('Candidate', 'Candidate'),
    ], max_length=10, null=True)
    pending_status = models.CharField(choices=[
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Rejected', 'Rejected'),
    ], max_length=10, null=True)
