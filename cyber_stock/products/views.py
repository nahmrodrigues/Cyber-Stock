# from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
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
        product_type = ProductType.objects.get(pk=self.kwargs['pk'])
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
    
class UpdateProduct(UpdateView):
    model = Product
    form_class = UpdateProductForm
    def get_product_type_id(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        product_type_id = product.product_type.id
        return product_type_id
    
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('products',
                            kwargs={'pk': self.get_product_type_id()},
                            current_app='products')

class ProductDetails(DetailView):
    model = Product
    context_object_name = 'product'
    
class DeleteProductType(DeleteView):
    queryset = ProductType.objects.all()
    success_url = reverse_lazy('product_types')

class DeleteProduct(DeleteView):
    queryset = Product.objects.all()
    success_url = reverse_lazy('product_types')

class BuyProduct(CreateView):
    model = ShoppingCart
    form_class = BuyProductForm
    success_url = reverse_lazy('buy_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ShoppingCart.objects.all()
        return context

class CheckoutShopping(CreateView):
    model = ShoppingCart
    fields = []

    def post(self, request, *args, **kwargs):
        cart_objects = ShoppingCart.objects.all()

        for cart_object in cart_objects:
            product = cart_object.product
            product.quantity_in_stock += cart_object.quantity
            product.save()
            cart_object.delete()

        return HttpResponseRedirect(reverse_lazy('product_types'))

def deleteProductFromCart(request, event_id):
    product = ShoppingCart.objects.get(pk=event_id)
    product.delete()
    return redirect('buy_product')
