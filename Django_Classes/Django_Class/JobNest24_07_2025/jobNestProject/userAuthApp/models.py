from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class userAuthModel(AbstractUser):
    user_types = models.CharField(choices=[
        ('recruiter', 'Recruiter'),
        ('jobseeker', 'Jobseeker'),
    ],max_length=20, null=True)
    
    def __str__(self):
        return self.username
    