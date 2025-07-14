from django.db import models

# Create your models here.
class BasicInfoModel(models.Model):
    username = models.CharField(max_length=30,null=True)
    fullName = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    addrees = models.CharField(max_length=100,null=True)
    profileImage = models.ImageField(upload_to='Media/profileImage',null=True)
