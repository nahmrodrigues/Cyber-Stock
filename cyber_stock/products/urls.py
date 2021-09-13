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
]