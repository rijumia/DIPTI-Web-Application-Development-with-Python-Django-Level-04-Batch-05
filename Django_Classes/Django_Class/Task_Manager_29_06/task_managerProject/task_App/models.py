from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    profile_picture = models.ImageField(upload_to='Media/profile', null=True)
    bio = models.TextField(null=True)

    
class TaskModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, null=True)
    TaskTitle = models.CharField(max_length=50, null=True)
    TaskDescription = models.TextField(null=True)
    TaskDueDate = models.DateField(null=True)
    TaskPriority = models.CharField(choices=[('low','Low'),('mediumn','Medium'),('high','High')],max_length=20, null=True)
    TaskStatus = models.CharField(choices=[('pending','Pending'),('in_progress','In_Progress'),('completed','Completed')],max_length=20, null=True)
    TaskCreateAt = models.DateTimeField(auto_now_add=True, null=True)
