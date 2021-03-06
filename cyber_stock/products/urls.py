from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
  path('<int:pk>/', ListProducts.as_view(template_name="list_products.html"), name="products"),
  path('create/', CreateProduct.as_view(template_name='create_product.html'), name='create_product'),
  path('details/<int:pk>', ProductDetails.as_view(template_name='product_details.html'), name='product_details'),
  path('types/', ListProductTypes.as_view(template_name="list_product_types.html"), name="product_types"),
  path('types/create/', CreateProductType.as_view(template_name='create_product_type.html'), name='create_product_type'),
  path('types/update/<int:pk>/', UpdateProductType.as_view(template_name='update_product_type.html'), name='update_product_type'),
  path('update/<int:pk>', UpdateProduct.as_view(template_name='update_product.html'), name='update_product'),
  path('types/delete/<int:pk>/', DeleteProductType.as_view(template_name='delete_product_type.html'), name='delete_product_type'),
  path('delete/<int:pk>/', DeleteProduct.as_view(template_name='delete_product.html'), name='delete_product'),
  path('buy/', BuyProduct.as_view(template_name='buy_product.html'), name='buy_product'),
  path('checkout_shopping/', CheckoutShopping.as_view(template_name='checkout_shopping.html'), name='checkout_shopping'),
  path('buy/delete/<event_id>', deleteProductFromShoppingCart, name='delete_shopping_cart_product'),
  path('sell/', SellProduct.as_view(template_name='sell_product.html'), name='sell_product'),
  path('sell/delete/<event_id>', deleteProductFromCart, name='delete_cart_product'),
  path('checkout_sales/', CheckoutSales.as_view(template_name='checkout_sales.html'), name='checkout_sales'),
  path('choose_register/', ChooseRegister.as_view(template_name='choose_register.html'), name='choose_register'),
]