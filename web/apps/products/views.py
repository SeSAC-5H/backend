from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from products.serializers import ProductCreateSerializer, BrandCreateSerializer, HashtagCreateSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

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
            # TODO: response를 출력하기 위한 LOGGER 추가
            data['message'] = "상품이 정상적으로 추가되었습니다."
        except Http404 as e:
            data['message'] = "brand_name이 등록되지 않았습니다."
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            data['message'] = str(e)
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data, status=status.HTTP_201_CREATED)

@extend_schema(
    tags=["상품"],
    summary="새로운 브랜드를 추가합니다.",
)
class BrandCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BrandCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        try:
            response = super().create(request, *args, **kwargs)
            # TODO: response를 출력하기 위한 LOGGER 추가
            data['message'] = "브랜드가 정상적으로 추가되었습니다."
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            data['message'] = str(e)
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
    tags=["상품"],
    summary="새로운 해시태그를 추가합니다.",
)
class HashtagCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = HashtagCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        try:
            response = super().create(request, *args, **kwargs)
            # TODO: response를 출력하기 위한 LOGGER 추가
            data['message'] = "해시태그가 정상적으로 추가되었습니다."
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            data['message'] = str(e)
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)