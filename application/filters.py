from django import forms
from .models import *
import django_filters


class LaptopFilter(django_filters.FilterSet):
    BRAND = (
        ('AC', 'Acer'),
        ('AS', 'Asus'),
        ('LV', 'Lenovo'),
        ('RZ', 'Razer')
    )
    brand = django_filters.MultipleChoiceFilter(field_name='brand', choices=BRAND, widget=forms.CheckboxSelectMultiple)

    RAM = (
        (4, '4gb'),
        (8, '8gb'),
        (16, '16gb'),
        (32,'32gb'),
    )
    price = django_filters.RangeFilter()
    ram = django_filters.MultipleChoiceFilter(field_name='ram', choices=RAM, widget=forms.CheckboxSelectMultiple)
    PROCESSOR_BRAND = (
        ('AMD', 'AMD'),
        ('INT', 'Intel')
    )
    processor_brand = django_filters.MultipleChoiceFilter(field_name='processor_brand', choices=PROCESSOR_BRAND, widget=forms.CheckboxSelectMultiple)
    TYPE = (
        ('TR', 'Traditional'),
        ('LW', 'Lightweight'),
        ('GM', 'Gaming')
    )
    type = django_filters.MultipleChoiceFilter(field_name='type', choices=TYPE, widget=forms.CheckboxSelectMultiple)
        


class PhoneFilter(django_filters.FilterSet):
    BRAND = (
        ('SM', 'Samsung'),
        ('XM', 'Xiaomi'),
        ('RM', 'Realme'),
        ('VV', 'Vivo')
    )
    brand = django_filters.MultipleChoiceFilter(field_name='brand', choices=BRAND, widget=forms.CheckboxSelectMultiple)
    PROCESSOR_BRAND = (
        ('SNP', 'Snapdragon'),
        ('MDT', 'MediaTek')
    )
    processor_brand = django_filters.MultipleChoiceFilter(field_name='processor_brand', choices=PROCESSOR_BRAND, widget=forms.CheckboxSelectMultiple)
    price = django_filters.RangeFilter()

class AccessoriesFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', widget=forms.TextInput)
    type = django_filters.CharFilter(field_name='type', widget=forms.TextInput)
    color = django_filters.CharFilter(field_name='color', widget=forms.TextInput)
    weight = django_filters.CharFilter(field_name='weight', widget=forms.TextInput)
    price = django_filters.RangeFilter()


