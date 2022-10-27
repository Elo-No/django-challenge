from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core.v1.models.match import Match
from core.v1.models.stadium import StadiumSeat
from utils.base_model import BaseModel

User = get_user_model()


class Tickt(BaseModel):

    STATUS_RESERVED = 0
    STATUS_PAID = 1
    _STATUS_CHOICES = (
        (STATUS_RESERVED, _('Reserved')),
        (STATUS_PAID, _('Paid')),
    )

    match = models.ForeignKey(
        verbose_name=_('Match'),
        to=Match,
        on_delete=models.CASCADE,
    )
    stadium_seat = models.ForeignKey(
        verbose_name=_('Seat'),
        to=StadiumSeat,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=User,
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=_STATUS_CHOICES,
        default=STATUS_RESERVED,
    )

    def __str__(self):
        return f'customer = {self.user} , match = {self.match}'

    class Meta:
        verbose_name = _('Tickt')
        verbose_name_plural = _('Tickt')
