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


class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('products')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        product_type = ProductType.objects.get(pk=form.data.get('product_type'))
        
        self.object = Product.objects.create(
            product_type=product_type,
            price=form.data.get('price'),
            brand=form.data.get('brand'),
            batch=form.data.get('batch'),
            description=form.data.get('description'),
        )
        
        return HttpResponseRedirect(self.get_success_url())