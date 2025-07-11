from django.db import models

class userModel(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Full_Name = models.CharField(max_length=200)
    User_Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Full_Name
    

