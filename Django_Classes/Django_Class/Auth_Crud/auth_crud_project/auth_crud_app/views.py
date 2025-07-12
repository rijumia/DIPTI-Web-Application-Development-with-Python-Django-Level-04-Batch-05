from django.shortcuts import render,redirect, HttpResponse
from auth_crud_app.models import CustomUserModel, ProductModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required
def homePage(request):


    return render(request, 'home.html')

def signUpPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        profileImage = request.FILES.get('profileImage')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
         user = CustomUserModel.objects.create_user(
            username=username,
            email=email,
            password=confirm_password,
            user_type=role,
            fullName=fullname,
            profileImage = profileImage,
          )
        return redirect('loginPage')
        
    return render(request, 'signup.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')

@login_required
def logOutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def addProduct(request):
    if request.user.user_type != 'owner':
        return HttpResponse('Permission Denied')
    
    if request.method == 'POST':
        pname = request.POST.get('pname')
        pdescription = request.POST.get('pdescription')
        price = request.POST.get('price')
        img = request.FILES.get('img')

        
        productinfo = ProductModel.objects.create(
            productName=pname,  
            productDescription=pdescription,
            productPrice=price,
            productImage=img
        )
        return redirect('listProduct')
    return render(request, 'addProduct.html')

@login_required
def updateProduct(request, id):
    if request.user.user_type != 'owner':
        return HttpResponse('Permission Denied')
    
    product = ProductModel.objects.get(id=id)
    if request.method == 'POST':
        product.productName = request.POST.get('pname')
        product.productDescription = request.POST.get('pdescription')
        product.productPrice = request.POST.get('price')
        if request.FILES.get('img'):
            product.productImage = request.FILES.get('img')
        product.save()
        return redirect('listProduct')
    
    return render(request, 'updateProduct.html', {'product': product})

@login_required
def listProduct(request):
    products = ProductModel.objects.all()
    return render(request, 'listProduct.html',{'products':products})

@login_required
def viewProduct(request, id):
    product = ProductModel.objects.get(id=id)
    return render(request, 'viewProduct.html',{'product':product})

@login_required
def deletePage(request,id):
    if request.user.user_type != 'owner':
        return HttpResponse('Permission Denied')
    product = ProductModel.objects.get(id=id)
    product.delete()
    return render(request, 'listProduct.html',{'product':product})


