from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from stores.serializers import StoreCreateSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.


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
