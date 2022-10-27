from rest_framework.serializers import ModelSerializer, ValidationError
from core.v1.models.stadium import StadiumSeat

from core.v1.models.tickt import Tickt
from utils.cache_function import getKey, ttlKey


class SeatSerializer(ModelSerializer):
    class Meta:
        model = StadiumSeat
        fields = ('id', 'stadium', 'stadium_seat_id')


class BuyTicktSerializer(ModelSerializer):
    class Meta:
        model = Tickt
        fields = ("id", 'match', 'stadium_seat', 'user', 'status')
