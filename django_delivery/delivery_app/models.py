from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title} - Precio: ${self.price}'
    
class Categories(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.title}'
    
class Coupons(models.Model):
    coupon =  models.CharField(max_length=32)
    discount = models.IntegerField()

    def __str__(self):
        return f'Cupón: {self.title} | Descuento: {self.price}%'
    
    