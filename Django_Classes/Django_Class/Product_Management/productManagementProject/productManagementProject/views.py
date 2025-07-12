from django.shortcuts import render, redirect
from productApp.models import*

def homePage(request):
    customerData = customerModel.objects.all()
    context = {
        'data' : customerData
    }
    return render(request, 'home.html', context)

def productPage(request):
    productData = productModel.objects.all()
    context = {
        'data' : productData
    }
    return render(request, 'product.html', context)

def addProductPage(request):
    
    if request.method=='POST':
        newproduct = productModel(
        name = request.POST.get["pname"],
        details = request.POST.get["details"],
        price = request.POST.get["price"],
        stock = request.POST.get["stock"],
        createdby = request.POST.get["createdby"],
        )
        newproduct.save()
        return redirect(request, 'product.html')
    
        
        
    
    
    
    
    return render(request, 'addProduct.html')