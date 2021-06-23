from .models import *
import django_filters

class LaptopFilter(django_filters.FilterSet):
    brand = django_filters.AllValuesFilter()
    price = django_filters.AllValuesFilter()
    ram = django_filters.AllValuesFilter()
    processor_model = django_filters.AllValuesFilter()
    os = django_filters.AllValuesFilter()
        


