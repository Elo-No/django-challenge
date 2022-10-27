from django.db import models
from django.utils.translation import gettext_lazy as _
from core.v1.models.stadium import Stadium
from utils.base_model import BaseModel


class Match(BaseModel):
    team_A = models.CharField(
        verbose_name=_('Host Team'),
        max_length=64
    )
    team_B = models.CharField(
        verbose_name=_('Guest Team'),
        max_length=64

    )
    stadium = models.ForeignKey(
        verbose_name=_('Stadium'),
        to=Stadium,
        on_delete=models.CASCADE,
    )
    which_salone = models.IntegerField(
        verbose_name=_('Number of Stadium Salone'))
    date_time = models.DateTimeField(verbose_name=_(
        'Date of Match'), null=True, blank=True)

    def __str__(self):
        return f'host = {self.host_team} , guest ={self.guest_team} in date = {self.date_time} at salone = {self.which_salone}'

    class Meta:
        unique_together = ('stadium', 'which_salone')
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')
