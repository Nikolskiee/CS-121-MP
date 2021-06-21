from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(null=True, blank=True, upload_to='product_images')
    
    def __str__(self):
        return str(self.name)

class Laptop(Product):
    BRAND = (
        ('AC', 'Acer'),
        ('AS', 'Asus'),
        ('LV', 'Lenovo'),

    )
    brand = models.CharField(choices=BRAND, null=True, blank=False, max_length=2)
    ram = models.IntegerField()
    storage = models.IntegerField()
    display = models.CharField(max_length=20, null=True, blank=False)
    display_size = models.CharField(max_length=20, null=True, blank=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    TYPE = (
        ('TR', 'Traditional'),
        ('LW', 'Lightweight'),
        ('GM', 'Gaming')
    )
    type = models.CharField(choices=TYPE, null=True, blank=False, max_length=2)



    