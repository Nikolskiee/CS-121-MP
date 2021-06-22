from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'application/index.html')

def laptops(request):
    laptops = Laptop.objects.all()
    data = { 'laptops': laptops }
    return render(request, 'application/laptops.html', data)

def smartphones(request):
    smartphones = Smartphone.objects.all()
    data = { 'smartphones' : smartphones }
    return render(request, 'application/smartphones.html', data)

def accessories(request):
    accessories = Accessories.objects.all()
    data = { 'accessories' : accessories }
    return render(request, 'application/accessories.html', data)

@login_required(login_url='/login')
def cart(request):
    return render(request, 'application/cart.html')

def signin(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print("Login was successful")
            return redirect('/')
        else:
            print("Login failed")
            messages.error(request, "Incorrect password or username.")

    return render(request, 'application/login.html')

def card(request):
    return render(request, 'application/card.html')

def cod(request):
    return render(request, 'application/cod.html')

def terms(request):
    return render(request, 'application/terms.html')

def privacy(request):
    return render(request, 'application/privacy.html')

def about(request):
    return render(request, 'application/about.html')

def laptopdetails(request, pk):
    if Laptop.objects.get(id=pk) is not None:
        product = Laptop.objects.get(id=pk)
    else:
        product = Product.objects.get(id=pk)  
    data = { 'product': product}
    return render(request, 'application/product_details.html', data)

def smartphonedetails(request, pk):
    if Smartphone.objects.get(id=pk) is not None:
        product = Smartphone.objects.get(id=pk)
    else:
        product = Product.objects.get(id=pk)
    data = { 'product': product}
    return render(request, 'application/product_details.html', data)

def accessoriesdetails(request, pk):
    if Accessories.objects.get(id=pk) is not None:
        product = Accessories.objects.get(id=pk)
    else:
        product = Product.objects.get(id=pk)
    data = { 'product': product}
    return render(request, 'application/product_details.html', data)

def signup(request):
    form = UserForm()

    if(request.method == "POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Account was created for " + form.cleaned_data.get("username"))
            return redirect('/login')
        
    data = {"form" : form}
    return render(request, 'application/signup.html', data)

def signout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'application/profile.html')