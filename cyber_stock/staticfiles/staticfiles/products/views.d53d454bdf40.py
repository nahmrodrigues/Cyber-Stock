# from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ListProductTypes(ListView):
    template_name = 'list_product_types.html'
    model = ProductType

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        
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
    template_name='create_product_type.html'
    model = ProductType

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('product_types')


class ListProducts(ListView):
    template_name='list_product_types.html'
    model = Product

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        product_type = ProductType.objects.get(pk=self.kwargs['pk'])
        products = Product.objects.filter(product_type=product_type)
        return products
        

class CreateProduct(CreateView):
    template_name='create_product.html'
    model = Product

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    form_class = CreateProductForm
    success_url = reverse_lazy('product_types')


class UpdateProductType(UpdateView):
    template_name='update_product_type.html'
    model = ProductType

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    fields = [
        'name',
        'description'
    ]
    success_url = reverse_lazy('product_types')
    
class UpdateProduct(UpdateView):
    template_name='update_product.html'
    model = Product

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
    template_name='product_details.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Product
    context_object_name = 'product'
    
class DeleteProductType(DeleteView):
    template_name='delete_product_type.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    queryset = ProductType.objects.all()
    success_url = reverse_lazy('product_types')

class DeleteProduct(DeleteView):
    template_name='delete_product.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    queryset = Product.objects.all()
    success_url = reverse_lazy('product_types')

class BuyProduct(CreateView):
    template_name='buy_product.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    model = ShoppingCart
    form_class = BuyProductForm
    success_url = reverse_lazy('buy_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ShoppingCart.objects.all()
        return context

@login_required
def deleteProductFromShoppingCart(request, event_id):

    product = ShoppingCart.objects.get(pk=event_id)
    product.delete()
    return redirect('buy_product')

class CheckoutShopping(CreateView):
    template_name='checkout_shopping.html'
    model = ShoppingCart

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

    fields = []

    def post(self, request, *args, **kwargs):
        cart_objects = ShoppingCart.objects.all()

        for cart_object in cart_objects:
            product = cart_object.product
            product.quantity_in_stock += cart_object.quantity
            product.save()
            cart_object.delete()

        return HttpResponseRedirect(reverse_lazy('product_types'))      

class SellProduct(CreateView):
    template_name='sell_product.html'
    model = SalesCart

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    form_class = SellProductForm
    success_url = reverse_lazy('sell_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = SalesCart.objects.all()
        return context

@login_required
def deleteProductFromCart(request, event_id):
    product = SalesCart.objects.get(pk=event_id)
    product.delete()
    return redirect('sell_product')
    

class ProductDetails(DetailView):
    template_name='product_details.html'
    model = Product
    context_object_name = 'product'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

class CheckoutSales(CreateView):
    template_name='checkout_sales.html'
    model = SalesCart
    fields = []

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        cart_objects = SalesCart.objects.all()

        for cart_object in cart_objects:
            product = cart_object.product
            product.quantity_in_stock -= cart_object.quantity
            if product.quantity_in_stock >= 0:
                product.save()
                cart_object.delete()
            elif product.quantity_in_stock < 0:
                #raise ValidationError("A quantidade de produtos é maior que a disponível no estoque !")
                return render(request, "checkout_sales.html", {'error':'O estoque não possui esta quantidade que você deseja! Escolha uma quantidade menor!'})


            

        return HttpResponseRedirect(reverse_lazy('product_types'))


class ChooseRegister(View):
    template_name='choose_register.html'
    def get(self, request):     
        return render(request, 'choose_register.html')