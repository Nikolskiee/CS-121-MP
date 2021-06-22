from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
    attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Password', 'required' : True ,}
    password1 = CharField(widget=PasswordInput(attrs=attrs))
    password2 = CharField(widget=PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter First Name', 'required' : True ,}),
            'last_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Last Name', 'required' : True ,}),
            'username' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Username', 'required' : True ,}),
            'email' : TextInput(attrs = { 'type' : 'email' , 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Email', 'required' : True ,})
            }

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity']

        widgets = {
            'user' : HiddenInput(attrs = {'type' : 'hidden'}),
            'product' : HiddenInput(attrs = {'type' : 'hidden'}),
            'quantity' : NumberInput(attrs = {'class': 'form-control', 'min' : '1'}),
        }