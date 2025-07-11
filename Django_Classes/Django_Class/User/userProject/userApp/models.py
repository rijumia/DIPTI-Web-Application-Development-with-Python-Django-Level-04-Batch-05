from django.db import models

class userModel(models.Model):
    User_First_Name = models.CharField(max_length=100)
    User_Last_Name = models.CharField(max_length=100)
    User_Name = models.CharField(max_length=200, null=True)
    User_Full_Name = models.CharField(max_length=200, null=True)
