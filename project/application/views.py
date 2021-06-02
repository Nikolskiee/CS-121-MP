from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'application/index.html')

def laptops(request):
    return render(request, 'application/laptops.html')

def smartphones(request):
    return render(request, 'application/smartphones.html')

def accessories(request):
    return render(request, 'application/accessories.html')

def cart(request):
    return render(request, 'application/cart.html')

def login(request):
    return render(request, 'application/login.html')

def signup(request):
    return render(request, 'application/signup.html')