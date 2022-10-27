from rest_framework.generics import CreateAPIView

from core.v1.permissions.has_federation_permission import IsFederationOrReadOnly
from core.v1.serializers.match_serializers import MatchSerializer


class CreateMatchAPIView(CreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = (IsFederationOrReadOnly, )
