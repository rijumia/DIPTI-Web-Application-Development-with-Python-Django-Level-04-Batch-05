from django.db import models

class recipeModel(models.Model):
    RecipeTitle = models.CharField(max_length=100)
    RecipeDesciption = models.TextField(max_length=500)
    RecipeIngredients = models.CharField(max_length=100)
    RecipeInstrauction = models.CharField(max_length=100)
    RecipeImage = models.ImageField(upload_to='Media/recipe')
