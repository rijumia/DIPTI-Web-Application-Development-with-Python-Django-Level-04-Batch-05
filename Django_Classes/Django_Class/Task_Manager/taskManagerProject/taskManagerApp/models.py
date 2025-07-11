from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    fullname = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    img = models.ImageField(upload_to='Media/profile')
    bio = models.TextField(max_length=200, null=True)
    password = models.CharField( null=True)


class TaskModel(models.Model):
    user = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,  null=True)
    TaskTitle = models.CharField(max_length=200, null=True)
    TaskDescription = models.TextField(max_length=200, null=True)
    TaskPriority = models.CharField(max_length=50, null=True)
    TaskStatus = models.CharField(max_length=50, null=True)
    TaskDueDate = models.DateField(null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)