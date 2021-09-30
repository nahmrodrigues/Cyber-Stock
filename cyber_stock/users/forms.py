from django import forms

class SignupManagerForm(forms.Form):  
    name = forms.CharField(required=True, label = 'Nome') 
    email = forms.EmailField(required=True, label = 'E-mail')
    password1 = forms.CharField(required=True, label = 'Senha', widget = forms.PasswordInput)
    password2 = forms.CharField(required=True, label = 'Confirme', widget = forms.PasswordInput)

class LoginForm(forms.Form):   
    email = forms.EmailField(required=True, label = 'E-mail')
    password = forms.CharField(required=True, label = 'Senha', widget = forms.PasswordInput)