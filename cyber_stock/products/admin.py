from django.contrib import admin
from .models import ProductType
from .models import Product

# Register your models here.
admin.site.register(ProductType)
admin.site.register(Product)