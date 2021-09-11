from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
  path('<int:id>/', ListProducts.as_view(template_name="list_products.html"), name="products"),
  path('create/', CreateProduct.as_view(template_name='create_product.html'), name='create_product'),
  path('types/', ListProductTypes.as_view(template_name="list_product_types.html"), name="product_types"),
  path('types/create/', CreateProductType.as_view(template_name='create_product_type.html'), name='create_product_type'),
  path('types/update/<int:pk>/', UpdateProductType.as_view(template_name='update_product_type.html'), name='update_product_type'),
  #path('', UpdateProduct.as_view(template_name='uptade_product.html'), name='update_product')
]