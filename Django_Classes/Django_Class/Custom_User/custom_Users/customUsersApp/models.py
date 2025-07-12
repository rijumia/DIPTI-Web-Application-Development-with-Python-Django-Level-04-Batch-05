from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    role = [
        ('seeker','Seeker'),
        ('recuiter', 'Recuiter')
    ]
    user_type = models.CharField(choices=role, max_length=10, null=True)
    age = models.PositiveIntegerField(null=True)
    mobile = models.CharField(max_length=20,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='Midea/img',null=True)
    instutiteName = models.CharField(max_length=100,null=True)
    passingYear = models.PositiveIntegerField(null=True)
    workExperience = models.PositiveSmallIntegerField(null=True)
