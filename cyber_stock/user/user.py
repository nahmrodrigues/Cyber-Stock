from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns =[
    path('signup/', CreateAdmin.as_view(template_name='signup.html'), name='signup'),
]