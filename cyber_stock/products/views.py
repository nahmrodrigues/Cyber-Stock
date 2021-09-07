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
    success_url = reverse_lazy('product_types')


class ListProducts(ListView):
    model = Product

    def get_queryset(self):
        product_type = ProductType.objects.get(pk=self.kwargs['id'])
        products = Product.objects.filter(product_type=product_type)
        return products
        

class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('product_types')


class UpdateProductType(UpdateView):
    model = ProductType
    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('product_types')
    
class DeleteProductType(DeleteView):
    queryset = ProductType.objects.all()
    success_url = reverse_lazy('product_types')