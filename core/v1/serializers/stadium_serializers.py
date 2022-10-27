
from rest_framework.serializers import ModelSerializer

from core.v1.models.stadium import Stadium


class StadiumSerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = ("id", "name", "number_salone", "capacity", "address")
        read_only_fields = ('id',)
