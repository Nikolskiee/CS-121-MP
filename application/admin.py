from application.models import Product
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Laptop)

admin.site.register(Smartphone)

admin.site.register(Accessories)

admin.site.register(Cart)