from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


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
def detail(request): 
    products = Product.objects.all()
    return render(request, 'detail.html', {'products': products})

# Authenticator
def register_user(req):
    form = SignUpForm()
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, "You have register success! Well come to Furni.")
            return redirect('login')
        else: 
            messages.success(req, "Have problem, please try again!")
            return redirect('login')
    return render(req, "register.html", {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged In"))
            return redirect('home')
        else: 
            messages.success(request, ("There was an error, try again"))
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout_user(request):
    logout(request)
    return redirect('login')