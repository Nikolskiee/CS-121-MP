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
        form = CartForm({"user": item.user.id, "product" : item.product.id, "quantity" : item.quantity})
        cart.append({"item" : item, "form" : form})
    
    shipping = 100
    total = shipping + subtotal
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
    form = CartForm({"user" : request.user.id, "product" : product.id, "quantity" : "1"})
    data["form"] = form
    return render(request, 'application/product_details.html', data)

def accessoriesdetails(request, pk):
    if Accessories.objects.get(id=pk) is not None:
        product = Accessories.objects.get(id=pk)
    else:
        product = Product.objects.get(id=pk)
    data = { 'product': product}
    form = CartForm({"user" : request.user.id, "product" : product.id, "quantity" : "1"})
    data["form"] = form
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
    data = {"cart" : cart, "subtotal" : subtotal, "count" : count, "total" : total, "shipping" : shipping}
    return render(request, 'application/checkout.html',data)

@login_required(login_url='/login')
def checkout_cart(request):
    subject = "MyShop Checkout Receipt"
    message = "Good Day! <br><br> Below is your Order Payment Slip. Due to a limited workforce in this period of quarantine, there may be delays in the processing of orders. <br> Thank you for your understanding."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    #send_mail(subject, message, from_email, recipient_list)
    
    email = EmailMessage(
        subject,
        message,
        from_email,
        recipient_list,
    )
    
    email.content_subtype = 'html'
    pdf = generate_pdf(request).getvalue()
    email.attach("receipt.pdf", pdf, 'application/pdf')
    #email.send()

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
        form = CartForm({"user": item.user.id, "product": item.product.id, "quantity": item.quantity})
        cart.append({"item": item, "form": form})

    context = {"user": request.user, "cart": cart, "sub_total": sub_total, "product_count": product_count}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="receipt.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pdf = pisa.CreatePDF(html, dest=response)
    
    if not pdf.err:
        return response
    