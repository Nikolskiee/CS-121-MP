from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Price (in php)')
    image = models.ImageField(null=True, blank=True, upload_to='product_images')

    carousel_image_1 = models.ImageField(null=True, blank=True, upload_to='product_images')
    carousel_image_2 = models.ImageField(null=True, blank=True, upload_to='product_images')
    carousel_image_3 = models.ImageField(null=True, blank=True, upload_to='product_images')

    
    def __str__(self):
        return str(self.name)

class Laptop(Product):
    os = models.CharField(max_length=100, null=True, blank=False)
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

    def get_instance(self):
        return 'laptop'

    def get_brand(self):
        return dict(self.BRAND).get(self.brand)
    
    def get_processor(self):
        return dict(self.PROCESSOR_BRAND).get(self.processor_brand)

    def get_laptop_type(self):
        return dict(self.TYPE).get(self.type)


class Smartphone(Product):
    BRAND = (
        ('SM', 'Samsung'),
        ('XM', 'Xiaomi'),
        ('RM', 'Realme'),
        ('VV', 'Vivo')
    )

    brand = models.CharField(choices = BRAND, null = True, blank = False, max_length = 2)
    PROCESSOR_BRAND = (
        ('SNP', 'Snapdragon'),
        ('MDT', 'MediaTek')
    )
    processor_brand = models.CharField(choices = PROCESSOR_BRAND, null = True, blank = False, max_length = 3)
    processor_model = models.CharField(max_length=100, null=True, blank=False)

    OS = (
        ('A10', 'Android 10'),
        ('A11', 'Android 11'),
        ('A12', 'Android 12')
    )
    os = models.CharField(choices = OS, null = True, blank = False, max_length = 3)
    ram = models.IntegerField(verbose_name = 'RAM (in GB)')
    storage = models.IntegerField(verbose_name = 'Storage (in GB)')
    display = models.CharField(max_length = 100, null = True, blank = False)

    def get_instance(self):
        return 'smartphone'

    def get_brand(self):
        return dict(self.BRAND).get(self.brand)
    
    def get_processor(self):
        return dict(self.PROCESSOR_BRAND).get(self.processor_brand)
    
    def get_os(self):
        return dict(self.OS).get(self.os)
    
class Accessories(Product):
    type = models.CharField(max_length = 100, null = True, blank = False)
    
    brand = models.CharField(max_length=100, null=True, blank=False)

    color = models.CharField(max_length=100, null=True, blank=False)

    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Weight (in grams)')

    def get_instance(self):
        return 'accessories'

