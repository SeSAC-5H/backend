from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from products.serializers import ProductCreateSerializer
from rest_framework.response import Response

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["상품"],
    summary="새로운 상품을 추가합니다.",
)
class ProductCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        try:
            response = super().create(request, *args, **kwargs)
            data = response.data.copy()
        except Exception as e:
            data['message'] = str(e)
        return Response(data)