from rest_framework.serializers import ModelSerializer

from core.v1.models.match import Match


class MatchSerializer(ModelSerializer):

    class Meta:
        model = Match
        fields = ("id", 'team_A', 'team_B', 'stadium',
                  'date_time', 'which_salone')
        read_only_fields = ('id',)
