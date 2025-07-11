from django.db import models

class blogModel(models.Model):
    blogTitle = models.CharField(max_length=200)
    blogAuthor = models.CharField(max_length=100)
    
