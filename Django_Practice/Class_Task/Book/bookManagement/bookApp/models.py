from django.db import models

class bookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    publishDate = models.DateField()
