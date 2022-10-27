from django.urls import path
from account.v1.views import ObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]