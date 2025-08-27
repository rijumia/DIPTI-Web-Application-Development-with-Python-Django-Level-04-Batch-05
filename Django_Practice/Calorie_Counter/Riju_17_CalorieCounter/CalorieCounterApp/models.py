from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserAuthModel(AbstractUser):

    def __str__(self):
        return self.username
    
class UserProfileModel(models.Model):
    user = models.OneToOneField(CustomUserAuthModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(choices=[
        ('Male', "Male"),
        ('Female', 'Female'),
    ], max_length=10, null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)

    def __str__(self):
        return self.name
    