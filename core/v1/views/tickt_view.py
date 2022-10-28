
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from core.v1.models import tickt
from core.v1.models.stadium import StadiumSeat

from core.v1.serializers.tickt_serializer import BuyTicktSerializer, SeatSerializer
from drf_yasg.utils import swagger_auto_schema
from utils.cache_function import get_all_key, getKey, setKey


class ListSeatAPIView(ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        reserved_seats = get_all_key()
        return StadiumSeat.objects.all().exclude(id__in=reserved_seats)


class BuyTicktAPIView(CreateAPIView):
    serializer_class = BuyTicktSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        setKey(instance.stadium_seat, tickt.STATUS_RESERVED, 60*10)
