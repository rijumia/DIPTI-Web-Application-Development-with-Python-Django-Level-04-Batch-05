from django.db import models
from users_auth_app.models import CustomUserModel
from employer_app.models import JobModel

# Create your models here.
class CandidateProfileModel(models.Model):
    candidate_user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='candidate_profile',null=True)
    full_name = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    address = models.TextField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.email
    
class JobApplicationModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name='job_application', null=True)
    candidate = models.ForeignKey(CandidateProfileModel, on_delete=models.CASCADE, related_name='job_candidate', null=True)
    last_education = models.CharField(max_length=50, null=True)
    work_experience = models.CharField(max_length=100, null=True)
    status = models.CharField(choices=[
        ('Applied','Applied'),
        ('Interview','Interview'),
        ('Offered','Offered'),
        ('Rejected','Rejected'),
        
    ],max_length=20, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.last_education
    