from django.db import models

class recipeModel(models.Model):
    RecipeTitle = models.CharField(max_length=100)
    RecipeDescription = models.CharField(max_length=200)
    RecipeIngrefients = models.CharField(max_length=300)
    RecipeInstructions = models.CharField(max_length=200)
    RecipeImage = models.ImageField(upload_to='Recipe/cover')
