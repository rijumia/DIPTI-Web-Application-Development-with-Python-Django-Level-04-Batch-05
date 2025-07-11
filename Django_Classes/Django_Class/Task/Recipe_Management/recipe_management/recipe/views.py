from django.shortcuts import render, redirect, HttpResponse
from recipe.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# <------------Authentication---------------->

def registerPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('loginPage')
    return render(request, 'registerPage.html')
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            return HttpResponse('username or password not matched')
        return redirect('home')
    return render(request, 'loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')



# <------------CRUD---------------->
@login_required
def home(request):
    recipeData = recipeModel.objects.all()
    return render(request, 'home.html', {'recipe': recipeData})
@login_required
def addRecipe(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        creator = request.POST.get('creator')
        description = request.POST.get('description')

        recipe = recipeModel(
            image = image,
            name = name,
            ingredients = ingredients,
            instructions = instructions,
            creator = creator,
            description = description,
        )
        recipe.save()
        return redirect('home')
    return render(request, 'addRecipe.html')
@login_required
def editRecipe(request,id):
    recipeData = recipeModel.objects.get(id=id)
    if request.method == 'POST':
        recipeData.name = request.POST.get('name')
        recipeData.ingredients = request.POST.get('ingredients')
        recipeData.instructions = request.POST.get('instructions')
        recipeData.creator = request.POST.get('creator')
        recipeData.description = request.POST.get('description')

        picture = request.FILES.get('image')
        if picture is not None:
            recipeData.image = picture
        recipeData.save()
        return redirect("home")
    return render(request, 'editRecipe.html', {'recipe': recipeData})
@login_required
def viewRecipe(request,id):
    recipeData = recipeModel.objects.get(id=id)
    return render(request, 'viewRecipe.html', {'recipe': recipeData})
@login_required
def deleteRecipe(request,id):
    recipe = recipeModel.objects.get(id=id)
    recipe.delete()
    return redirect('home')