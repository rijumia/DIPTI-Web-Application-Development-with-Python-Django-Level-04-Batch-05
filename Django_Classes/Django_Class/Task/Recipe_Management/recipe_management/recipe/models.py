from django.db import models

# Create your models here.
class recipeModel(models.Model):
    image = models.ImageField(upload_to='media/recipes', null=True)
    name = models.CharField(max_length=100, null=True)
    ingredients = models.TextField(null=True)
    instructions = models.TextField(null=True)
    creator = models.CharField(max_length=100, null=True)
    description =models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)