from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _

class ProductType(models.Model):

    class Meta:
        verbose_name = _("Tipo de Produto")
        verbose_name_plural = _("Tipos de Produtos")
    
    name = models.CharField(
        verbose_name=_("Nome"),
        unique = True,
        max_length=50,
        blank=False
    )

    description = models.TextField(
        verbose_name=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )

class Product(models.Model):
    """
    Abstract class that represents class 'Component' in Composite Pattern.
    """

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")
    
    product_type = models.ForeignKey(
        ProductType,
        related_name="product_type",
        verbose_name=_("Tipo de Produto"),
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    price = models.FloatField(
        verbose_name=_("Preço"),
        validators=[validators.MinValueValidator(0)],
        blank=False,
        null=False
    )

    brand = models.CharField(
        verbose_name=_("Marca"),
        max_length=50,
        blank=False,
        null=False
    )

    batch = models.PositiveIntegerField(
      verbose_name=_("Lote"),
      blank=False,
      null=False
    )

    description = models.TextField(
        verbose_name=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )

    quantity_in_stock = models.PositiveIntegerField(
      verbose_name=_("Quantidade em Estoque"),
      default=0,
      editable=True,
      blank=False,
      null=False
    )

class ShoppingCart(models.Model):

    class Meta:
        verbose_name = _("Produto no Carrinho de Compras")
        verbose_name_plural = _("Produtos no Carrinho de Compras")

    product = models.ForeignKey(
        Product,
        related_name="product",
        verbose_name=_("Produto"),
        on_delete=models.RESTRICT,
        blank=False,
        null=False
    )

    quantity = models.PositiveIntegerField(
      verbose_name=_("Quantidade"),
      default=0,
      editable=True,
      blank=False,
      null=False
    )

    provider = models.CharField(
        verbose_name=_("Provedor"),
        max_length=50,
        blank=False,
        null=False
    )
