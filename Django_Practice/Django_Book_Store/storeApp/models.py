from django.db import models

class userModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField(max_length=11)
    
class bookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    publishDate = models.DateField()
