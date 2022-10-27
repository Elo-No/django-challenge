from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import BaseModel


class Address(BaseModel):
    zip_code = models.CharField(
        verbose_name=_('ZIP / Postal code'),
        max_length=128,
        null=True,
        blank=True
    )

    city = models.CharField(
        verbose_name=_('City'),
        max_length=128,
        null=True,
        blank=True
    )

    country = models.CharField(
        verbose_name=_('Country'),
        max_length=128,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
