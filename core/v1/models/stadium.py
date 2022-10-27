from django.db import models
from django.utils.translation import gettext_lazy as _
from core.v1.models.address import Address

from utils.base_model import BaseModel


class Stadium(BaseModel):
    name = models.CharField(
        verbose_name=_('Stadium name'),
        max_length=64,
    )
    capacity = models.IntegerField(
        verbose_name=_('Capacity'),
    )
    number_salone = models.IntegerField(
        verbose_name=_('Number Salone'),
        null=True, blank=True,
    )
    address = models.OneToOneField(to=Address, null=True, blank=True,
                                   on_delete=models.SET_NULL, verbose_name=_("Address"))

    def __str__(self):
        return f'name = {self.name}'

    class Meta:
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')


class StadiumSeat(BaseModel):
    stadium = models.ForeignKey(
        verbose_name=_('Stadium'),
        to='Stadium',
        on_delete=models.CASCADE,
        related_name='seat_places',

    )

    stadium_seat_id = models.IntegerField(verbose_name=_('Stadium seat ID'))
    row = models.IntegerField(verbose_name=_(
        'Row of stadium seat place'), null=True, blank=True)
    column = models.IntegerField(
        verbose_name=_('Column of stadium seat place'), null=True, blank=True)

    def __str__(self):
        return f'seat id = {self.stadium_seat_id}, stadium = {self.stadium.id}'

    class Meta:
        unique_together = ('stadium_seat_id', 'stadium')
        verbose_name = _('Stadium seats')
        verbose_name_plural = _('Stadium seats')
