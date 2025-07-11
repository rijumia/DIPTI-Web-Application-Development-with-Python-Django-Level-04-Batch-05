from django.db import models

class UserAuthModel(models.Model):
    UserName = models.CharField(max_length=50)
    FullName= models.CharField(max_length=100)
    Email = models.EmailField()
    ContactNo = models.CharField(max_length=11)
    Password = models.CharField(max_length=10)
    CreatedAt = models.DateTimeField(auto_now_add=True)
