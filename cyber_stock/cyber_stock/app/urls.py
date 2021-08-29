from django.urls import path
from .views import Index, CadastrarTipos

urlpatterns = [
  path('', Index.as_view(), name="list"),
  path('cadastrarTipos/', CadastrarTipos.as_view(), name="cadastrarTipos"),
]
