from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    brand = models.CharField(max_length=100, null=True, blank=False)
    description = models.CharField(max_length=100, null=True, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return str(self.name)