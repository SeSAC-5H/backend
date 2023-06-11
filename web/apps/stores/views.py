from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from stores.serializers import (
    StoreCreateSerializer,
    StoreSerializer,
    ReportCreateSerializer,
)
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from stores.models import Stores
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from geopy.distance import distance

# Create your views here.


@extend_schema(
    tags=["상점"],
    summary="상점 상세정보를 조회 및 추가합니다.",
    parameters=[
        OpenApiParameter(
            name="lat",
            description="위도를 입력해주세요. ex) lat=37.61196834",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="lon",
            description="경도를 입력해주세요, ex)lon=127.07948812",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="distance",
            description="검색할 반경을 입력해주세요. 디폴트 150m 입니다.",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        ),
    ],
)
class StoreListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = StoreCreateSerializer
    stores = Stores.objects.exclude(store_subcate="1")

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
        meter = 100
        if "distance" in queryParams:
            meter = int(queryParams["distance"])

        if "lon" in queryParams and "lat" in queryParams:
            user_location = (
                float(queryParams["lat"]),
                float(queryParams["lon"]),
            )
            near_stores = []
            for store in self.stores:
                store_location = (
                    float(store.store_coord_y),
                    float(store.store_coord_x),
                )
                if distance(user_location, store_location).m <= meter:
                    serializer = StoreSerializer(store)
                    near_stores.append(
                        {
                            "store": serializer.data,
                            "distance": distance(
                                user_location, store_location
                            ).m,
                        }
                    )
            return Response(near_stores, status=status.HTTP_200_OK)
        else:
            serializer = StoreSerializer(self.stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=["상점"],
    summary="상점정보를 추가합니다.",
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "report_name": {"type": "string"},
                "report_address": {"type": "string"},
                "report_tel": {"type": "string"},
            },
        },
    },
)
class ReportCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReportCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        try:
            super().create(request, *args, **kwargs)
            data["message"] = "상점이 정상적으로 추가되었습니다."
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
