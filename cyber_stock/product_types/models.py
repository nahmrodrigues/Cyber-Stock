from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class ProductType(models.Model):

    class Meta:
        verbose_name = _("Tipo de Produto")
        verbose_name_plural = _("Tipos de Produtos")
    
    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Nome"),
        max_length=50,
        blank=False
    )

    description = models.TextField(
        verbose_name=_("Descrição"),
        help_text=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )