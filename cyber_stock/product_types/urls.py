from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
  path('', ListProductTypes.as_view(template_name="list.html")),
  path('create', CreateProductType.as_view(template_name='form.html'), name='create_product_type'),
]