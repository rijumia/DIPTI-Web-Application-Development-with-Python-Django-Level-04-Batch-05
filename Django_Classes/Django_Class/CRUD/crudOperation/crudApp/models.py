from django.db import models

class userModel(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Age = models.IntegerField(max_length=3)
    Email = models.EmailField()
    Address = models.TextField(max_length=100)
