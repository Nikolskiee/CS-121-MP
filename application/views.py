from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'application/index.html')

def laptops(request):
    laptops = Laptop.objects.all()
    data = { 'laptops': laptops }
    return render(request, 'application/laptops.html', data)

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

def details(request, pk):
    product = Product.objects.get(id=pk)
    data = { 'product': product}
    return render(request, 'application/product_details.html', data)