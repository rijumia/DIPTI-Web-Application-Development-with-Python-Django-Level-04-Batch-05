from django.db import models

class customerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

class productModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

