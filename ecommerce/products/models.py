from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.TextField(blank=True)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name="products")
    def __str__(self):
        return self.name