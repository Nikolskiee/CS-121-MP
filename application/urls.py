"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('laptops/', views.laptops, name="laptops"),
    path('smartphones/', views.smartphones, name="smartphones"),
    path('accessories/', views.accessories, name="accessories"),
    path('cart/', views.cart, name="cart"),
    path('login/', views.signin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('payment/card', views.card, name="card"),
    path('payment/cod', views.cod, name='cod'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('about/', views.about, name='about'),
    path('laptop/details/<str:pk>/', views.laptopdetails, name='laptopdetails'),
    path('smartphones/details/<str:pk>/', views.smartphonedetails, name='smartphonedetails'),
    path('accessories/details/<str:pk>', views.accessoriesdetails, name='accessoriesdetails'),
    path('logout/', views.signout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('cart/add', views.addcart, name="addcart"),
    path('cart/remove/<str:pk>', views.removecart, name="removecart"),
    path('cart/update/<str:pk>', views.update_cart, name="updatecart"),

    path('receipt/', views.generate_pdf, name="receipt")
]
