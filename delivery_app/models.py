from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to = 'category_images', null = True, blank = True)

    def __str__(self):
        return f'{self.title}'
    
class Products(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField(null = True)
    image = models.ImageField(upload_to = 'product_images', null = True, blank = True)

    def __str__(self):
        return f'{self.title} - Precio: ${self.price}'

class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    comment = models.TextField(max_length=5000, null = True)
    star_rating = models.IntegerField()
    created_at = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return f'{self.author.username} - {self.title}'