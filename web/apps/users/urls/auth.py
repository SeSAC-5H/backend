from django.urls import path
from users.views import TokenBlackListAPIView, TokenCreateAPIView, TokenRefreshAPIView

app_name = "auth"

urlpatterns = [
    path("tokens/", TokenCreateAPIView.as_view()),
    path("tokens/refresh/", TokenRefreshAPIView.as_view()),
    path("tokens/blacklist/", TokenBlackListAPIView.as_view()),
]