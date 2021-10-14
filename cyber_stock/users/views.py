# Django imports
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils.decorators import method_decorator

# Local imports
from .forms import *
from .models import *
from .decorators import *

class SignupManagerView(View):
    
    @method_decorator(is_manager_or_superuser)
    def get(self, request):
        data = { 'form': SignupManagerForm() }     
        return render(request, 'signup.html', data)
    
    @method_decorator(is_manager_or_superuser)
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

            # a variavel 'next' contem a url da proxima pagina
            # entao se ela existir, redirecionamos para essa url apos logar
            # caso contrario, vamos para a pagina inicial
            if user is not None and 'next' in request.POST: 
                login(request, user)
                return HttpResponseRedirect(request.POST.get('next'))
            elif user is not None:
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

class RegisterEmployeeView(View):

    @method_decorator(is_manager)
    def get(self, request):
        data = { 'form': RegisterEmployeeForm() }     
        return render(request, 'register_employee.html', data)
        
    @method_decorator(is_manager)
    def post(self, request):
        form = RegisterEmployeeForm(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            Employee.objects.create_user(email=email, password=password, name=name)
            return HttpResponseRedirect(reverse('product_types'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }  

        return render(request, 'register_employee.html', data)

class UsersList(ListView):
    model = User

    @method_decorator(is_manager)
    def get(self, request):
        data = { 'object_list': self.get_queryset() }     
        return render(request, 'users_list.html', data)
    
    def get_queryset(self):
        users = User.objects.all()
        return users