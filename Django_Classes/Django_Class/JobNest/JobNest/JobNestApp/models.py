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
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    ]

    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    deadline = models.DateField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True, null=True)
    company_location = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

    
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='jobseeker_profile')
    resume = models.FileField(upload_to='media/profile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class JobApplication(models.Model):
    jobseeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(CreateJobModel, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)