from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from django.template.loader import get_template
from xhtml2pdf import pisa

import math

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
    subtotal = 0
    count = 0
    for item in items:
        subtotal = subtotal + (item.quantity * item.product.price)
        count = count + item.quantity
        pretotal = 0
        x = 0
        while x < item.quantity:
            pretotal += item.product.price
            x += 1
        form = CartForm({"user": item.user.id, "product" : item.product.id, "quantity" : item.quantity})
        cart.append({"item" : item, "form" : form, "pretotal" : pretotal})
    
    shipping = 100
    total = shipping + subtotal
    user = request.user
    data = {"cart" : cart, "subtotal" : subtotal, "count" : count, "total" : total, "shipping" : shipping}
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

@login_required(login_url='/login')
def update_cart(request, pk):
    single_cart = Cart.objects.get(id=pk)
    form = CartForm(request.POST, instance=single_cart)
    if (form.is_valid()):
        form.save()
    
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

@login_required(login_url='/login')
def card(request):
    
    try:
        details = User_Details.objects.get(user=request.user)
        form1 = UserDetailsForm(instance=details)
        details.payment_option = "Credit Card"

    except User_Details.DoesNotExist:
        form1 = UserDetailsForm({"user": request.user.id})

    try:
        credit = User_Credit.objects.get(user=request.user)
        form2 = CreditForm(instance=credit)

    except User_Credit.DoesNotExist:
        form2 = CreditForm({"user": request.user.id})

    if(request.method == "POST"):
        try:
            details = User_Details.objects.get(user=request.user)
            form1 = UserDetailsForm(request.POST or None, instance=details)
            details.payment_option = "Credit Card"

        except User_Details.DoesNotExist:
            form1 = UserDetailsForm(request.POST)

        try:
            credit = User_Credit.objects.get(user=request.user)
            form2 = CreditForm(request.POST or None, instance=credit)

        except User_Credit.DoesNotExist:
            form2 = CreditForm(request.POST)
        
        if(form1.is_valid() and form2.is_valid()):
            form1.save()
            form2.save()

            return redirect('/checkout')

    data = {"form1": form1, "form2": form2}
    return render(request, 'application/card.html', data)

@login_required(login_url='/login')
def cod(request):
    try:
        details = User_Details.objects.get(user=request.user)
        form = UserDetailsForm(instance=details)
        details.payment_option = "Cash On Delivery"

    except User_Details.DoesNotExist:
        form = UserDetailsForm({"user": request.user.id})

    if(request.method == "POST"):
        try:
            details = User_Details.objects.get(user=request.user)
            form = UserDetailsForm(request.POST or None, instance=details)
            details.payment_option = "Cash On Delivery"

        except User_Details.DoesNotExist:
            form = UserDetailsForm(request.POST or None)
        
        if(form.is_valid()):
            form.save()
            return redirect('/checkout')

    data = {"form": form}
    return render(request, 'application/cod.html', data)

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

    comments = product.comment_set.all()

    if ( len(comments) != 0 ):
        overall_rating = 0
        for comment in comments:
            overall_rating += comment.rating 
        overall_rating = overall_rating/len(comments)
        data = {'product': product, 'comments':comments, 'overall_rating': round(overall_rating), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer(),}
    else: 
        data = {'product': product, 'rating_floor' : 0 }
    
    form = CartForm({"user" : request.user.id, "product" : product.id, "quantity" : "1"})
    commentform = CommentForm({"user" : request.user.id, "product" : product.id, "comment" : "", "rating" : "0"})
    data["commentform"] = commentform
    data["form"] = form
    data["totalreviews"] = len(comments)
    return render(request, 'application/product_details.html', data)



def smartphonedetails(request, pk):
    if Smartphone.objects.get(id=pk) is not None:
        product = Smartphone.objects.get(id=pk)
    else:
        product = Product.objects.get(id=pk)
    
    comments = product.comment_set.all()

    if ( len(comments) != 0 ):
        overall_rating = 0
        for comment in comments:
            overall_rating += comment.rating 
        overall_rating = overall_rating/len(comments)
        data = {'product': product, 'comments':comments, 'overall_rating': round(overall_rating), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer(),}
    else: 
        data = {'product': product, 'rating_floor' : 0 } 

    form = CartForm({"user" : request.user.id, "product" : product.id, "quantity" : "1"})
    commentform = CommentForm({"user" : request.user.id, "product" : product.id, "comment" : "", "rating" : "0"})
    data["commentform"] = commentform
    data["form"] = form
    data["totalreviews"] = len(comments)
    return render(request, 'application/product_details.html', data)

def accessoriesdetails(request, pk):
    if Accessories.objects.get(id=pk) is not None:
        product = Accessories.objects.get(id=pk)
    else:
        product = Product.objects.get(id=pk)
    
    comments = product.comment_set.all()

    if ( len(comments) != 0 ):
        overall_rating = 0
        for comment in comments:
            overall_rating += comment.rating 
        overall_rating = overall_rating/len(comments)
        data = {'product': product, 'comments':comments, 'overall_rating': round(overall_rating), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer(),}
    else: 
        data = {'product': product, 'rating_floor' : 0 }

    form = CartForm({"user" : request.user.id, "product" : product.id, "quantity" : "1"})
    commentform = CommentForm({"user" : request.user.id, "product" : product.id, "comment" : "", "rating" : "0"})
    data["commentform"] = commentform
    data["form"] = form
    data["totalreviews"] = len(comments)
    return render(request, 'application/product_details.html', data)

def signup(request):
    form = UserForm()

    if(request.method == "POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Account was created for " + form.cleaned_data.get("username"))
            subject = "Account Creation Confirmation"
            message = "Good Day! " + request.POST.get("username") + ", <br><br> This is to confirm that an your account was successfully created."
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email")]

            email = EmailMessage (
                subject, 
                message,
                from_email,
                recipient_list,
            )

            email.content_subtype = "html"

            email.send()
            return redirect('/login')
        
    data = {"form" : form}
    return render(request, 'application/signup.html', data)

def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'application/profile.html')

@login_required(login_url='/login')
def addreview(request, pk):
    form = CommentForm(request.POST)

    if (form.is_valid()):
        form.save()

        return redirect("/")

@login_required(login_url='/login')
def removereview(request, pk):
    single_comment = Comment.objects.get(id=pk)
    single_comment.delete()
    return redirect("/")


@login_required(login_url='/login')
def checkout(request):
    items = Cart.objects.filter(user = request.user).order_by('id')
    cart = []
    subtotal = 0
    count = 0
    for item in items:
        subtotal = subtotal + (item.quantity * item.product.price)
        count = count + item.quantity
        form = CartForm({"user": item.user.id, "product" : item.product.id, "quantity" : item.quantity})
        cart.append({"item" : item, "form" : form})
    
    shipping = 100
    total = shipping + subtotal
    user_details = User_Details.objects.get(user=request.user)
    data = {"cart" : cart, "subtotal" : subtotal, "count" : count, "total" : total, "shipping" : shipping, "user_details": user_details}
    return render(request, 'application/checkout.html',data)

@login_required(login_url='/login')
def placeorder(request):
    subject = "DVD-R Kween Receipt"
    message = "Good Day! " + request.user.username + ", <br><br> Below is your Invoice Slip. Expect the package to be delivered at you after 7 working days. Thank you."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]

    email = EmailMessage(
        subject, 
        message,
        from_email,
        recipient_list
    )



    email.content_subtype = "html"
    pdf = generate_pdf(request).getvalue()
    email.attach("receipt.pdf", pdf, 'application/pdf')
    email.send()

    items = Cart.objects.filter(user = request.user).order_by('id')
    for item in items:
        item.delete()

    return redirect("/cart")



@login_required(login_url='/login')
def generate_pdf(request):
    template_path = 'application/receipt.html'

    items = Cart.objects.filter(user=request.user).order_by('id')
    cart = []
    sub_total = 0
    product_count = 0
    for item in items:
        sub_total = sub_total + (item.quantity * item.product.price)
        product_count = product_count + item.quantity
        pretotal = 0
        x = 0
        while x < item.quantity:
            pretotal += item.product.price
            x += 1
        form = CartForm({"user": item.user.id, "product" : item.product.id, "quantity" : item.quantity})
        cart.append({"item" : item, "form" : form, "pretotal" : pretotal})

    user_details = User_Details.objects.get(user=request.user)
    context = {"user": request.user, "cart": cart, "sub_total": sub_total, "product_count": product_count, "user_details": user_details}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="receipt.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pdf = pisa.CreatePDF(html, dest=response)
    
    if not pdf.err:
        return response
    