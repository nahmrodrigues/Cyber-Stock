from django import forms
from .models import *


class CreateProductForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = [
        'product_type',
        'price',
        'brand',
        'batch',
        'description'
    ]

  def __init__(self, *args, **kwargs):
    super(CreateProductForm, self).__init__(*args, **kwargs)
    self.fields['product_type'] = forms.ChoiceField(choices=self.get_product_types_names)

  def get_product_types_names(self):
    names = []
    for product_type in ProductType.objects.all():
      names.append((product_type.id, product_type.name))
    
    return names
