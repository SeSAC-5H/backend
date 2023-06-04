# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views as jwt_views

from users.serializers import UserCreateSerializer

class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

class TokenCreateAPIView(jwt_views.TokenObtainPairView):
    pass

class TokenRefreshAPIView(jwt_views.TokenRefreshView):
    pass
    
class TokenBlackListAPIView(jwt_views.TokenBlacklistView):
    pass