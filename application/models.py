from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Price (in php)')
    image = models.ImageField(null=True, blank=True, upload_to='product_images')
    
    def __str__(self):
        return str(self.name)

class Laptop(Product):
    BRAND = (
        ('AC', 'Acer'),
        ('AS', 'Asus'),
        ('LV', 'Lenovo'),
        ('RZ', 'Razer')
    )
    brand = models.CharField(choices=BRAND, null=True, blank=False, max_length=2)
    PROCESSOR_BRAND = (
        ('AMD', 'AMD'),
        ('INT', 'Intel')
    )
    processor_brand = models.CharField(choices=PROCESSOR_BRAND, null=True, blank=False, max_length=3)
    processor_model = models.CharField(max_length=100, null=True, blank=False)
    graphics_card = models.CharField(max_length=100, null=True, blank=False)
    ram = models.IntegerField(verbose_name='RAM (in gb)')
    storage = models.IntegerField(verbose_name='Storage (in gb)')
    display = models.CharField(max_length=100, null=True, blank=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Weight (in Kg)')
    TYPE = (
        ('TR', 'Traditional'),
        ('LW', 'Lightweight'),
        ('GM', 'Gaming')
    )
    type = models.CharField(choices=TYPE, null=True, blank=False, max_length=2)



    