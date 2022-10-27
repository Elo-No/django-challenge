from rest_framework.generics import CreateAPIView

from ..permissions.has_federation_permission import IsFederationOrReadOnly

from ..models.stadium import Stadium, StadiumSeat
from ..serializers.stadium_serializers import StadiumSerializer


class CreateStadiumAPIView(CreateAPIView):
    serializer_class = StadiumSerializer
    permission_classes = (IsFederationOrReadOnly, )

    def perform_create(self, serializer):
        instance = serializer.save()
        stadium = Stadium.objects.get(id=instance.id)
        StadiumSeat.objects.bulk_create([
            StadiumSeat(stadium_seat_id=seat_id, stadium=stadium) for seat_id in
            range(1, stadium.capacity)
        ])
        return instance
