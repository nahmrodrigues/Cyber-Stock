# from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

class ListProductTypes(ListView):
    model = ProductType

    def get_queryset(self):
        product_types = ProductType.objects.all()

        queryset = []

        for product_type in product_types:
            products = Product.objects.filter(product_type=product_type)
            queryset.append({
                'product_type': product_type, 
                'products_qtd': len(products)
            })

        return queryset



class CreateProductType(CreateView):
    model = ProductType
    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('products/types/')


class ListProducts(ListView):
    model = Product

    # def get_queryset(self):
    #     products = Product.objects.all()

    #     queryset = {}

    #     for product in products:
    #         name = product.product_type.name
    #         if name not in queryset.keys():
    #             queryset[name] = [product]
    #         else:
    #             queryset[name].append(product)

    #     return queryset
        

class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('products')