from django.urls import path

from ..views.stadium_views import CreateStadiumAPIView
from ..views.match_view import CreateMatchAPIView
urlpatterns = [
    path("stadium/", CreateStadiumAPIView.as_view(), name="create_stadium"),
    path("match/", CreateMatchAPIView.as_view(), name="create_match"),

]
