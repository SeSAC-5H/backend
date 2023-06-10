from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from stores.serializers import StoreCreateSerializer, StoreSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from stores.models import Stores
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema, OpenApiExample


# Create your views here.


@extend_schema(
    tags=["상점"],
    summary="상점 상세정보를 조회 및 추가합니다.",
    parameters=[
        OpenApiParameter(
            name="store_type",
            description="상점 타입을 지정해 주세요.",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            examples=[
                OpenApiExample(
                    name="1-카페",
                ),
                OpenApiExample(
                    name="1-식당",
                ),
                OpenApiExample(
                    name="3-리필샵",
                ),
                OpenApiExample(
                    name="4-생필품",
                ),
                OpenApiExample(
                    name="5-기타",
                ),
                OpenApiExample(
                    name="없음-전체",
                ),
            ],
        ),
    ],
)
class StoreListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = StoreCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        try:
            response = super().create(request, *args, **kwargs)
            # TODO: response를 출력하기 위한 LOGGER 추가
            data["message"] = "상점이 정상적으로 추가되었습니다."
        except Http404 as e:
            data["message"] = "store_name이 등록되지 않았습니다."
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            data["message"] = str(e)
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryParams = request.query_params
        if "store_type" in queryParams:
            storeType = queryParams["store_type"]
            serializer = StoreSerializer(
                Stores.objects.filter(store_subcate=storeType), many=True
            )
        else:
            serializer = StoreSerializer(Stores.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
