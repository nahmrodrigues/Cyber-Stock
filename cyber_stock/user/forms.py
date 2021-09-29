from django import forms
from .models import *
from django.core.exceptions import ValidationError
##from django.forms import *

class CreateProductForm(forms.ModelForm):

  class Meta:
    model = Admin
    fields = [
        'user',
        'password'
    ]
    widgets = {
      'user': forms.TextInput(attrs={
        'class': "",
        'placeholder': 'Usuário'
      }),
      'password': forms.TextInput(attrs={
        'class': "", 
        'placeholder': 'Senha'
      })}