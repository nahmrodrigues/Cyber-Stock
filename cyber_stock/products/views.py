# from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect

from .models import ProductType

class ListProductTypes(ListView):
    model = ProductType

class CreateProductType(CreateView):
    model = ProductType
    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('product_types')