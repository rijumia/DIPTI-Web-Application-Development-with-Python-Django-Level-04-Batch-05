from django.db import models

class customerModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=150)
    email = models.EmailField()
    age = models.IntegerField()
    
class productModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    createby = models.CharField(max_length=50)