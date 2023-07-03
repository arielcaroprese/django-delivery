from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.shortcuts import get_object_or_404

from django.views.generic import DeleteView, DetailView

from accounts import forms
from .models import UserMeta

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = forms.UserRegister(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            return render(request, 'accounts/user_register.html', {'form':form})
    form = forms.UserRegister()
    return render(request, 'accounts/user_register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not  None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/user_login.html', {'mensaje':"Datos incorrectos"})
    form = AuthenticationForm()
    return render(request, 'accounts/user_login.html', {'form':form})

class Logout(LogoutView):
    template_name = 'accounts/user_logout.html'


@login_required
def userEdit(request):

    user_actual = request.user

    if request.method == 'POST':

        form = forms.UserEdit(request.POST, request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            
            user_actual.email = data['email']
            user_actual.first_name = data['first_name']
            user_actual.last_name = data['last_name']
            user_actual.save()

            user = User.objects.get(username = request.user)
            usermeta = UserMeta.objects.get(user_id = user)
            usermeta.avatar = form.cleaned_data['avatar']
            usermeta.save()

            return redirect('home')
        else:
            form = forms.UserEdit()
    
    else:
        form = forms.UserEdit(
            initial={
                'email': user_actual.email,
                'first_name': user_actual.first_name,
                'last_name': user_actual.last_name,
            })
    return render(request, 'accounts/user_edit.html', {'form': form, "user": user_actual})


class UserDetailView(DetailView):
    model = User
    template_name = "accounts/user_detail.html"

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

"""

def user_delete(request):

"""