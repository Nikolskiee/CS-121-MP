import math

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from products.models import *
from products.forms import *

# Create your views here.

# BOOK RELATED CONTROLLERS

def home(request):
    books = Book.objects.all()
    items = []

    for book in books:
        form = ShoppingCartForm({"user": request.user.id, "book": book.id, "quantity": 1})
        items.append({"book": book, "form": form})

    data = {"items": items}
    return render(request, 'products/home.html', data)

def book(request,pk):
    book = Book.objects.get(id=pk)
    comments = book.comment_set.all()
 
    if ( len(comments) != 0 ):
        overall_rating = 0
        for comment in comments:
            overall_rating += comment.rating 
        overall_rating = overall_rating/len(comments)
        data = {'book': book, 'comments':comments, 'overall_rating': round(overall_rating,2), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer()}
    else: 
        data = {'book': book } 
    
    form = ShoppingCartForm({"user": request.user.id, "book": book.id, "quantity": 1})
    data["form"] = form            
    return render(request, 'products/book.html', data)

# CART RELATED CONTROLLERS

@login_required(login_url='/login')
def cart(request):
    items = ShoppingCart.objects.filter(user=request.user)
    cart = []
    cum_price = 0
    book_count = 0
    for item in items:
        cum_price = cum_price + (item.quantity * item.book.price)
        book_count = book_count + item.quantity
        form = ShoppingCartForm({"user": item.user.id, "book": item.book.id, "quantity": item.quantity})
        cart.append({"item":item, "form": form})

    data = {"cart": cart, "cum_price": cum_price, "book_count": book_count}
    return render(request, 'products/cart.html', data)

def add_cart(request):
    form = ShoppingCartForm(request.POST)
    if( form.is_valid() ):
        form.save()
        return redirect("/cart")

def update_cart(request, pk):
    single_cart = ShoppingCart.objects.get(id=pk)
    form = ShoppingCartForm(request.POST, instance=single_cart)
    if ( form.is_valid() ):
        form.save()
    
    return redirect("/cart")

def remove_cart(request, pk):
    single_cart = ShoppingCart.objects.get(id=pk)
    single_cart.delete()
    return redirect("/cart")

# USER AUTHENTICATION RELATED CONTROLLERS

def register(request):
    form = UserForm()

    if( request.method == "POST"):
        form = UserForm(request.POST)
        if( form.is_valid() ):
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            return redirect('/login')

    data = {"form": form}
    return render(request, 'products/register.html', data)

def login_page(request):
    if( request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("Login Success.")
            return redirect('/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")

    return render(request, 'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('login')