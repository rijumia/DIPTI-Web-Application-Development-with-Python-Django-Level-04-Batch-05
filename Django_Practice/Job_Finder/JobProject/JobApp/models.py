from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[
        ('recruiter', 'recruiter'),
        ('seeker', 'Seeker')
    ], max_length=10, null=True)
    phone_no = models.CharField(max_length=15, null=True)
    Bio = models.TextField(null=True)

    def __str__(self):
        return self.user_type

class JobModel(models.Model):
    JobTitle = models.CharField(max_length=50, null=True)
    JobDescription = models.TextField(null=True)
    CompanyLogo = models.ImageField(upload_to='Media/ComapnyLogo',null=True)
    Job_type = models.CharField(choices=[
        ('full_time', 'Full Time'),
        ('part_time','Part Time'),
    ], max_length=10,null=True)
    CreateBy = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)

