from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserMeta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatars', null = True, blank = True, default='delivery_app/static/delivery_app/assets/img/avatar.jpg')

    def __str__(self):
        return f"{self.user} - {self.avatar}"
