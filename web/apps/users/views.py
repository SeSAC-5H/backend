# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views as jwt_views

from users.serializers import UserCreateSerializer

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["사용자"],
    summary="새로운 사용자를 추가합니다.",
    # examples = USER_CREATE_EXAMPLES,
)
class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

@extend_schema(
    tags=["인증"],
    summary="Access/Refresh Token을 받습니다.",
)
class TokenCreateAPIView(jwt_views.TokenObtainPairView):
    pass

@extend_schema(
    tags=["인증"],
    summary="Refresh Token을 받습니다.",
)
class TokenRefreshAPIView(jwt_views.TokenRefreshView):
    pass
    
@extend_schema(
    tags=["인증"],
    summary="Refresh Token을 제거합니다.",
)
class TokenBlackListAPIView(jwt_views.TokenBlacklistView):
    pass