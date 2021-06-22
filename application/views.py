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
    items = Cart.objects.filter(user = request.user).order_by('id')
    cart = []
    total = 0
    count = 0
    for item in items:
        total = total + (item.quantity * item.product.price)
        count = count + item.quantity
        form = CartForm({"user": item.user.id, "product" : item.product.id, "quantity" : item.quantity})
        cart.append({"item" : item, "form" : form})
    
    data = {"cart" : cart, "total" : total, "count" : count}
    return render(request, 'application/cart.html', data)

@login_required(login_url='/login')
def addcart(request):
    form = CartForm(request.POST)

    if (form.is_valid()):
        form.save()
        return redirect("/cart")

@login_required(login_url='/login')
def removecart(request, pk):
    single_cart = Cart.objects.get(id=pk)
    single_cart.delete()
    return redirect("/cart")


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
    form = CartForm({"user" : request.user.id, "product" : product.id, "quantity" : "1"})
    data["form"] = form
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

@login_required(login_url='/login')
def profile(request):
    return render(request, 'application/profile.html')