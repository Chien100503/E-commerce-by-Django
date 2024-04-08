from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
def about(request):   
    return render(request, 'about.html')
def services(request):   
    return render(request, 'services.html')
def blog(request):   
    return render(request, 'blog.html')
def contact(request):   
    return render(request, 'contact.html')
def cart(request):   
    return render(request, 'cart.html')
def checkout(request):   
    return render(request, 'checkout.html')