from django.shortcuts import render, redirect
from productApp.models import*

def homePage(request):
    customerData = customerModel.objects.all()
    context = {
        'data': customerData
    }

    return render(request, 'home.html', context)

def productPage(request):
    productData = productModel.objects.all()
    context = {
        'data': productData
    }
    return render(request, 'products.html', context)

def addProduct(request):

    if request.method == 'POST':
        # productName = request.POST.get('product_name')
        # productDescription = request.POST.get('product_details')
        # productPrice = request.POST.get('price')
        # productqty = request.POST.get('qty')
        # created_at = request.POST.get('created_date')

        newProduct = productModel(
            name = request.POST.get('product_name'),
            description = request.POST.get('product_details'),
            price = request.POST.get('price'),
            stock = request.POST.get('qty'),
            created_at = request.POST.get('created_date'),
        )
        newProduct.save()
        return redirect('productPage')

    return render(request, 'addProduct.html')