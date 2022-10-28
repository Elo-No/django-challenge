from django.urls import path

from ..views.stadium_views import CreateStadiumAPIView
from ..views.match_view import CreateMatchAPIView
from ..views.tickt_view import BuyTicktAPIView, ListSeatAPIView
urlpatterns = [
    path("stadium/", CreateStadiumAPIView.as_view(), name="create_stadium"),
    path("match/", CreateMatchAPIView.as_view(), name="create_match"),
    path('match/available-seat/', ListSeatAPIView.as_view(), name="availble_seats"),
    path("match/buy-tickt/", BuyTicktAPIView.as_view(), name="buy_tickt"),

]
