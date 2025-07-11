from django.shortcuts import render, redirect, HttpResponse
from recipeApp.models import recipeModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def homePage(req, id):
    recipe = recipeModel.objects.get(id=id)

    return render(req, 'home.html', {'recipe': recipe})

@login_required
def addPage(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        description = req.POST.get('description')
        ingredients = req.POST.get('ingredients')
        instructions = req.POST.get('instructions')
        RecipeImage = req.FILES.get('RecipeImage')

        recipe = recipeModel(
            RecipeTitle = title,
            RecipeDesciption = description,
            RecipeIngredients = ingredients,
            RecipeInstrauction = instructions,
            RecipeImage = RecipeImage,
        )
        recipe.save()
        return redirect('listPage') 

    return render(req, 'add.html')

@login_required
def updatePage(req, id):
    recipe = recipeModel.objects.get(id=id)

    if req.method == 'POST':
        recipe.RecipeTitle = req.POST.get('title')
        recipe.RecipeDesciption = req.POST.get('description')
        recipe.RecipeIngredients = req.POST.get('ingredients')
        recipe.RecipeInstrauction = req.POST.get('instructions')
        if req.FILES.get('RecipeImage'):
            recipe.RecipeImage = req.FILES.get('RecipeImage')
        recipe.save()
        return redirect('updatePage', id=recipe.id)
    return render(req, 'update.html', {'recipedata': recipe})

@login_required
def listPage(req):
    recipes = recipeModel.objects.all()
    return render(req, 'list.html', {'recipes': recipes})

def deletePage(req, id):
    recipe = recipeModel.objects.get(id=id)
    recipe.delete()
    return redirect('listPage')


def loginPage(req):
    if req.method == 'POST':
        Username = req.POST.get('username')
        Password = req.POST.get('password')

        user = authenticate(username=Username,password=Password)

        if user:
            login(req, user)
            return redirect('addPage')

    return render(req, 'login.html')

def signinPage(req):

    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect('loginPage')
        else:
            return redirect('wrongPage')
    return render(req, 'signup.html')

def logoutPage(req):
    logout(req)
    return redirect('loginPage')

def wrongPage(req):
    return render(req, 'wrong.html')

