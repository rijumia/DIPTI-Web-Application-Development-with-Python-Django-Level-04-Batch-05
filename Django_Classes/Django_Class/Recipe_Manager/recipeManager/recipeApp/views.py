from django.shortcuts import render, redirect
from recipeApp.models import recipeModel

def home(req):
    recipes = recipeModel.objects.all()

    return render(req, 'home.html', {'recipes': recipes})

def addRecipe(req):
    recipes = recipeModel.objects.all()

    if req.method == 'POST':
        title = req.POST.get('recipeTitle')
        description = req.POST.get('recipeDescription')
        ingredients = req.POST.get('recipeIngredients')
        instructions = req.POST.get('recipeInstructions')
        image = req.FILES.get('recipeImage')
        recipe = recipeModel(
            RecipeTitle = title,
            RecipeDescription = description,
            RecipeIngrefients = ingredients,
            RecipeInstructions = instructions,
            RecipeImage = image
        )
        recipe.save()
        return redirect('recipeList')
    return render(req, 'addRecipe.html', {'recipes':recipes})

def editRecipe(req, id):
    recipes = recipeModel.objects.get(id=id)
    if req.method == 'POST':
        recipes.title = req.POST.get('recipeTitle')
        recipes.description = req.POST.get('recipeDescription')
        recipes.ingredients = req.POST.get('recipeIngredients')
        recipes.instructions = req.POST.get('recipeInstructions')
        if req.FILES.get('recipeImage'):
            recipes.image = req.FILES.get('recipeImage')
        return redirect('recipeList')
    recipes.save()
    return render(req, 'editRecipe.html')

def recipeList(req):
    recipes = recipeModel.objects.all()
    return render(req, 'recipeList.html', {'recipes':recipes})

def viewRecipe(req, id):
    recipe = recipeModel.objects.get(id=id)
    return render(req, 'viewRecipe.html', {'recipe':recipe})

def deleteRecipe(req, id):
    recipe = recipeModel.objects.get(id=id)
    recipe.delete()
    return redirect('recipeList')