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

    """
    def get_queryset(self):
        

        products = Product.objects.all()

        queryset = {}

        for product in products:
            name = product.product_type.name
            if name is not in queryset.keys():
                queryset[name].products = [product]
                queryset[name].brands[product.brand] = 1
            else:
                queryset[name].append(product)

                if product.brand is not in queryset[name].brands:
                    

        for 

        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset
    """
        

class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('products')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        try:
            product_type = ProductType.objects.get(pk=form.data.get('product_type'))
        
            self.object = Product.objects.create(
                product_type=product_type,
                price=form.data.get('price'),
                brand=form.data.get('brand'),
                batch=form.data.get('batch'),
                description=form.data.get('description'),
            )
        
            return HttpResponseRedirect(self.get_success_url())
        except:
            self.object = None
            return self.form_invalid(form)