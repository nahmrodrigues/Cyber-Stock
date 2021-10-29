from django import forms
from .models import *
from django.core.exceptions import ValidationError
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

  def clean_product_type(self):
      data = self.cleaned_data['product_type']

      if not ProductType.objects.filter(pk=data).exists():
        raise ValidationError("O tipo de produto não existe!")
      else:
        data = ProductType.objects.get(pk=data)

      return data

  def clean(self):
    cleaned_data = super(CreateProductForm, self).clean()

    product_type = cleaned_data.get('product_type')
    brand = cleaned_data.get('brand')

    if Product.objects.filter(
      product_type=product_type,
      brand=cleaned_data.get('brand')
    ).exists():
      raise ValidationError("O produto já existe!")

    return cleaned_data

  
class UpdateProductForm(forms.ModelForm):

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
    super(UpdateProductForm, self).__init__(*args, **kwargs)
    self.fields['product_type'] = forms.ChoiceField(
      required=True, label="Tipo de Produto", 
      choices=self.get_product_types_names
    )

  def get_product_types_names(self):
    names = []
    for product_type in ProductType.objects.all():
      names.append((product_type.id, product_type.name))
    
    return names

  def clean_product_type(self):
      data = self.cleaned_data['product_type']

      if not ProductType.objects.filter(pk=data).exists():
        raise ValidationError("O tipo de produto não existe!")
      else:
        data = ProductType.objects.get(pk=data)

      return data

  def clean(self):
    cleaned_data = super(UpdateProductForm, self).clean()
    
    return cleaned_data


class BuyProductForm(forms.ModelForm):

  class Meta:
    model = ShoppingCart
    fields = [
        'product',
        'quantity'
    ]

  def __init__(self, *args, **kwargs):
    super(BuyProductForm, self).__init__(*args, **kwargs)
    
    self.fields['product'] = forms.ChoiceField(
      required=True, label="Produto", 
      choices=self.get_products
    )

    self.fields['quantity'] = forms.IntegerField(
      required=True,
      label="Quantidade",
      min_value=0
    )

  def get_products(self):
    products = []
    for product in Product.objects.all():
      choice = product.product_type.name + " - " + product.brand
      products.append((product.id, choice))
    
    return products

  
  def clean_product(self):
      data = self.cleaned_data['product']

      if not Product.objects.filter(pk=data).exists():
        raise ValidationError("O produto não existe!")
      else:
        data = Product.objects.get(pk=data)

      return data

  def clean(self):
    cleaned_data = super(BuyProductForm, self).clean()
    
    return cleaned_data

class SellProductForm(forms.ModelForm):

  class Meta:
    model = SalesCart
    fields = [
        'product',
        'quantity'
    ]

  def __init__(self, *args, **kwargs):
    super(SellProductForm, self).__init__(*args, **kwargs)
    
    self.fields['product'] = forms.ChoiceField(
      required=True, label="Produto", 
      choices=self.get_products
    )

    self.fields['quantity'] = forms.IntegerField(
      required=True,
      label="Quantidade",
      min_value=0
    )

  def get_products(self):
    products = []
    for product in Product.objects.all():
      choice = product.product_type.name + " - " + product.brand
      products.append((product.id, choice))
    
    return products

  
  def clean_product(self):
      data = self.cleaned_data['product']

      if not Product.objects.filter(pk=data).exists():
        raise ValidationError("O produto não existe!")
      else:
        data = Product.objects.get(pk=data)

      return data

  def clean(self):
    cleaned_data = super(SellProductForm, self).clean()
    
    return cleaned_data
