from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Admin(models.Model):
    """
    Abstract class that represents class 'Component' in Composite Pattern.
    """

    class Meta:
        verbose_name = _("Administrador")
        verbose_name_plural = _("Administradores")
    

    user = models.CharField(
        verbose_name=_("Usuário"),
        max_length=50,
        blank=False,
        null=False
    )

    password = models.CharField(
        verbose_name=_("Senha"),
        max_length=50,
        blank=False,
        null=False
    )