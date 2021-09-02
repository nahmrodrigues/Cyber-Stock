# from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

class ListProductTypes(ListView):
    model = ProductType


class CreateProductType(CreateView):
    model = ProductType
    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('products/types/')


class ListProducts(ListView):
    model = Product

    def get_queryset(self):
        products = Product.objects.all()

        queryset = {}

        for product in products:
            name = product.product_type.name
            if name not in queryset.keys():
                queryset[name] = [product]
            else:
                queryset[name].append(product)

        return queryset
        

class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('products')