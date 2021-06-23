from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput, widgets
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
            'username' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'username', 'placeholder' : 'Enter Username', 'required' : True ,}),
            'email' : TextInput(attrs = { 'type' : 'email' , 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'email', 'placeholder' : 'Enter Email', 'required' : True ,})
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

class CODForm(ModelForm):
    class Meta:
        model = User_COD
        fields = ['province', 'municipality', 'barangay', 'hs_num']

        widgets = {
            'province' : HiddenInput(attrs = {'type' : 'hidden'}),
            'municipality' : HiddenInput(attrs = {'type' : 'hidden'}),
            'barangay' : HiddenInput(attrs = {'type' : 'hidden'}),
            'hs_num' : HiddenInput(attrs = {'type' : 'hidden'})
        }

class CreditForm(ModelForm):
    class Meta:
        model = User_Credit
        fields = ['province', 'municipality', 'barangay', 'hs_num', 'full_name', 'card_number', 'mm', 'dd', 'yyyy', 'ccv']

        widgets = {
            'province' : HiddenInput(attrs = {'type' : 'hidden'}),
            'municipality' : HiddenInput(attrs = {'type' : 'hidden'}),
            'barangay' : HiddenInput(attrs = {'type' : 'hidden'}),
            'hs_num' : HiddenInput(attrs = {'type' : 'hidden'}),
            'full_name' : HiddenInput(attrs = {'type' : 'hidden'}),
            'card_number' : NumberInput(attrs = {'class': 'form-control'}),
            'mm' : NumberInput(attrs = {'class': 'form-control', 'min' : '1', 'max': '12'}),
            'dd' : NumberInput(attrs = {'class': 'form-control', 'min' : '1', 'max': '31'}),
            'yyyy' : NumberInput(attrs = {'class': 'form-control', 'min' : '0', 'max': '2021'}),
            'ccv' : NumberInput(attrs = {'class': 'form-control', 'min' : '0', 'max' : '999'})
        }