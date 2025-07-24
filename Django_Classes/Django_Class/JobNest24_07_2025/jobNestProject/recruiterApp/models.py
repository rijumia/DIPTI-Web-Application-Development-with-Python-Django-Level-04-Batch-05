from django.db import models
from userAuthApp.models import *

# Create your models here.
class RecruiterProfileModel(models.Model):
    recruiter_user = models.OneToOneField(userAuthModel, on_delete=models.CASCADE, related_name='recruiter_profile', null=True)
    company_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    about_company = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='Media/company_logos/', null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.company_name
    
    
class JobModel(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Remote', 'Remote'),
        ('Internship', 'Internship'),
    ]

    recruiter = models.ForeignKey(RecruiterProfileModel,on_delete=models.CASCADE,related_name='job_post',null=True)
    title = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES,null=True)
    deadline = models.DateField(null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    posted_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
