from django.db import models

# Create your models here.
class newsModel(models.Model):
    thumbnail = models.ImageField(upload_to='media/images', null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    published_date = models.DateField(null=True)