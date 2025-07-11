from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    display_name=models.CharField(max_length=100,null=True)
    USER_TYPE={
        ('seeker','Job Seeker'),
        ('recruiter','Job Recruiter'),
    }
    user_type=models.CharField(choices=USER_TYPE,max_length=100,null=True)
    
    def __str__(self):
        return self.username

class RecruiterModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,null=True,related_name='recruitermodel')
    company_logo=models.ImageField(upload_to='media/company_logo',null=True)
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.user.username

class SeekerModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,null=True,related_name='seekermodel')
    skill_sets=models.CharField(max_length=100)
    resume=models.FileField(upload_to='media/resume',null=True)
    def __str__(self):
        return self.user.username
    
class JobModel(models.Model):
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True,related_name='jobmodel')
    title=models.CharField(max_length=100,null=True)
    number_of_openings=models.IntegerField(null=True)
    category=models.CharField(max_length=100,null=True)
    job_description=models.TextField(null=True)
    skill_sets=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title

class JobApplyModel(models.Model):
    applicant=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    applied_job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    skills=models.CharField(max_length=100)
    resume=models.FileField(upload_to='media/seeker_resume',null=True)
    status=models.CharField(max_length=100,default="Pending",null=True)
    
    def __str__(self):
        return self.applicant.username
