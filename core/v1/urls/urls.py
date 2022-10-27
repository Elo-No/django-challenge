from django.urls import path

from ..views.stadium_views import CreateStadiumAPIView

urlpatterns = [
    path("stadium/", CreateStadiumAPIView.as_view(), name="create_stadium"),
]
