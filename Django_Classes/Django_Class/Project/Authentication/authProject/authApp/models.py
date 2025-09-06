from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):

    def __str__(self):
        return self.username

class ProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True, related_name='profile')
    fullName = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=15, null=True)
    profilePhoto = models.ImageField(upload_to='profile-photo/', null=True)

    def __str__(self):
        return self.user.username if self.user else "No User"
    