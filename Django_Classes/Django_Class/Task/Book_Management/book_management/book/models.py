from django.db import models

# Create your models here.
class bookModel(models.Model):
    bookImage = models.ImageField(upload_to='media/images')
    title =models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    description =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)