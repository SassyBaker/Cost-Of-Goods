from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


class Stores(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Products(models.Model):
    barcode = models.CharField(max_length=256)
    sku = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    weight_unit = models.CharField(max_length=256, choices=(('kg', 'kg'), ('lb', 'lb'), ('oz', 'oz'), ('l', 'l'), ('ml', 'ml')))

    location = models.ForeignKey(Stores, on_delete=models.DO_NOTHING)
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    last_update = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=256)

    def __str__(self):
        return self.brand + self.product_name

    class Meta:
        ordering = ['sku']
