from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
  path('types/', ListProductTypes.as_view(template_name="list_product_types.html")),
  path('types/create/', CreateProductType.as_view(template_name='create_product_type.html'), name='create_product_type'),
]