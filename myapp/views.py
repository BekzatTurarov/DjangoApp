import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    return HttpResponse("Hello America!")

def products(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request, 'index.html', context)

def product_detail(request, id):
    context = {
        'product':Product.objects.get(id=id)
    }
    return render(request, 'detail.html', context)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        product = Product(name=name, price=price, desc=desc)
        product.save()
    return render(request, 'addproduct.html')

def update_product(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(request, 'updateproduct.html')
