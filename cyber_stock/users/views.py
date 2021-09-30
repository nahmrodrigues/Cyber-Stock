from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import Manager

class SignupManagerView(View):
    
    def get(self, request):
        data = { 'form': SignupManagerForm() }     
        return render(request, 'signup.html', data)
        
    def post(self, request):
        form = SignupManagerForm(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            if password1 == password2:
                Manager.objects.create_user(email=email, password=password1, name=name)
                return HttpResponseRedirect(reverse('login'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }  

        return render(request, 'signup.html', data)

class LoginView(View):
    def get(self, request):
        data = { 'form': LoginForm() }
        return render(request, 'login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        
        data = { 
            'form': form,
            'error': 'E-mail ou senha inválidos'
        }     
        return render(request, 'login.html', data)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))