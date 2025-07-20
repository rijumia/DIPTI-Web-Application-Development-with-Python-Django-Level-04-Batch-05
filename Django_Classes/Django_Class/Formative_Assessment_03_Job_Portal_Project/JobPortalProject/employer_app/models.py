from django.db import models
from users_auth_app.models import *

# Create your models here.

class EmployerProfileModel(models.Model):
    employer_user = models.OneToOneField(CustomUserModel , on_delete=models.CASCADE,null=True, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    about_company = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='Media/company_logos/', null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.company_name


from django.db import models

class JobModel(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Remote', 'Remote'),
        ('Internship', 'Internship'),
    ]

    employer = models.ForeignKey(EmployerProfileModel,on_delete=models.CASCADE,related_name='jobs',null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    deadline = models.DateField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
