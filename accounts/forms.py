from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserMeta

class UserRegister(UserCreationForm):
    email = forms.EmailField(label='Correo')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        help_texts = { key: '' for key in fields}

class UserEdit(forms.Form):
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(label='Avatar')

    class Meta:
        model = User 
        fields = ["email", "last_name", "first_name", "avatar"]

class AvatarEdit(forms.Form):
    avatar = forms.ImageField(label='Avatar')

    class Meta:
        model = UserMeta 
        fields = ["avatar"]
