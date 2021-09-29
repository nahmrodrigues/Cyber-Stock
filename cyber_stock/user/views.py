# from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.

class CreateAdmin(CreateView):
    model = Admin
    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('product_types')