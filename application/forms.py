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
        fields = ['user', 'province', 'municipality', 'barangay', 'hs_num']

        widgets = {
            'user' : HiddenInput(attrs = {'type' : 'hidden'}),
            'province' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Province', 'required' : True ,}),
            'municipality' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Municipality', 'required' : True ,}),
            'barangay' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Barangay', 'required' : True ,}),
            'hs_num' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter House and Street Number', 'required' : True ,})
        }

class CreditForm(ModelForm):
    class Meta:
        model = User_Credit
        fields = ['user', 'province', 'municipality', 'barangay', 'hs_num', 'full_name', 'card_number', 'mm', 'dd', 'yyyy', 'ccv']

        widgets = {
            'user' : HiddenInput(attrs = {'type' : 'hidden'}),
            'province' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Province', 'required' : True ,}),
            'municipality' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Municipality', 'required' : True ,}),
            'barangay' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Barangay', 'required' : True ,}),
            'hs_num' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter House and Street Number', 'required' : True ,}),
            'full_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Full Name', 'required' : True ,}),
            'card_number' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Card Number', 'required' : True ,}),
            'mm' : NumberInput(attrs = {'class': 'form-control', 'min' : '1', 'max': '12', 'required': True}),
            'dd' : NumberInput(attrs = {'class': 'form-control', 'min' : '1', 'max': '31', 'required': True}),
            'yyyy' : NumberInput(attrs = {'class': 'form-control', 'min' : '1950', 'max': '2050', 'required': True}),
            'ccv' : NumberInput(attrs = {'class': 'form-control', 'min' : '100', 'max' : '999', 'required': True})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'comment', 'rating']
        widgets = {
            'user' : HiddenInput(attrs = {'type' : 'hidden'}),
            'product' : HiddenInput(attrs = {'type' : 'hidden'}),
            'comment' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Comment', 'required' : True ,}),
            'rating' : NumberInput(attrs = {'class': 'form-control', 'min' : '0', 'max' : '5', 'required': True})
        }