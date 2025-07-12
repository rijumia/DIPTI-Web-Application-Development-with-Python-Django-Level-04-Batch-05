from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[
        ('Recruiter', 'Recruiter'),
        ('Seeker', 'Seeker'),
    ],max_length=10, null=True)
    phone_no = models.PositiveIntegerField(max_length=15,null=True)
    bio = models.TextField(null=True)
    fullName = models.CharField(max_length=50, null=True)
    
class JobModel(models.Model):
    JobTitle = models.CharField(max_length=100, null=True)
    JobDescription = models.TextField(max_length=200, null=True)
    CompanyLogo = models.ImageField(upload_to='Media/companyLogo', null=True)
    JopType = models.CharField(choices=[
        ('PartTime', 'PartTime'),
        ('FullTime','FullTime'),
    ],max_length=10, null=True)
    Created_By = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE, null=True)
