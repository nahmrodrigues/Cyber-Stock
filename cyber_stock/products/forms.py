from django import forms
from .models import *
##from django.forms import *

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
    widgets = {
      'product_type': forms.Select(attrs={
        'class': "create-product-input",
        'placeholder': 'Tipo de Produto'
      }),
      'price': forms.NumberInput(attrs={
        'class': "create-product-input", 
        'placeholder': 'Preço'
      }),
      'brand': forms.TextInput(attrs={
        'class': "create-product-input",
        'placeholder': 'Marca'
      }),
      'batch': forms.NumberInput(attrs={
        'class': "create-product-input",
        'placeholder': 'Lote'
      }),
      'description': forms.Textarea(attrs={
        'class': "create-product-input",
        'placeholder': 'Descrição'
      })
    }

  def __init__(self, *args, **kwargs):
    super(CreateProductForm, self).__init__(*args, **kwargs)
    self.fields['product_type'] = forms.ChoiceField(
      required=True, label="Tipo de Produto", 
      choices=self.get_product_types_names
    )

  def get_product_types_names(self):
    names = []
    for product_type in ProductType.objects.all():
      names.append((product_type.id, product_type.name))
    
    return names

  
