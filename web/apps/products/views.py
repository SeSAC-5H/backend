from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from products.serializers import ProductCreateSerializer, BrandCreateSerializer, HashtagCreateSerializer, ProductHashtagCreateSerializer, ProductSerializer, HashtagSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.db.models import Count
from products.models import Product, Hashtag, ProductHashtag, HashtagCategory

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view
from drf_spectacular.utils import extend_schema
from products.paginations import ProductPagination

from products.permissions import IsUserOrReadonly

@extend_schema(
    tags=["상품"],
)
class ProductModelViewSet(ModelViewSet):
    permission_classes = [IsUserOrReadonly]
    pagination_class = ProductPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer
        return ProductSerializer

    @extend_schema(
        summary="상품을 조회합니다.",
        parameters=[
            OpenApiParameter(
                name="hash_seq",
                description="해시태그 순번을 지정해 주세요.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="page",
                description="페이지 순번입니다.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="page_size",
                description="한 페이지에 표시할 개체 수입니다.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        queryParams = request.query_params
        page = 1
        pageSize = 10
        if 'page' in queryParams:
            page = int(queryParams['page'])
        if 'page_size' in queryParams:
            pageSize = int(queryParams['page_size'])
        startIdx = (page - 1) * pageSize
        endIdx = startIdx + pageSize

        prodData = []
        if 'hash_seq' in queryParams:
            hashSeq = queryParams['hash_seq']
            hashQ = get_object_or_404(Hashtag, hash_seq=hashSeq)
            prodHashQs = ProductHashtag.objects.select_related('prod_seq').filter(hash_seq=hashQ.hash_seq)
            prodSeqList = [
                prodHashQ.prod_seq.prod_seq
                for prodHashQ in prodHashQs
            ]
            prodQs = Product.objects.select_related('brand_seq').filter(prod_seq__in=prodSeqList)
            prodSerializer = ProductSerializer(prodQs, many=True)

            totalProductCnt = len(prodSerializer.data)
            prodData = prodSerializer.data[startIdx:endIdx]

        else:
            totalProductCnt = Product.objects.all().count()
            prodSerializer = ProductSerializer(Product.objects.all()[startIdx:endIdx], many=True)
            prodData = prodSerializer.data
        
        retData = {
            'data': prodData,
            'total_pages': (totalProductCnt + pageSize - 1) // pageSize,
            'page': page
        }
        
        return Response(retData, status=status.HTTP_200_OK)

    @extend_schema(
        summary="상품을 생성합니다.",
        examples=[
            OpenApiExample(
                "Valid example 1",
                summary="테스트 상품 생성 예시",
                description="인증이 확인된 사용자만 상품을 생성할 수 있습니다.",
                value={
                    "prod_name": "테스트",
                    "prod_link": "http://",
                    "prod_price": 10000,
                    "prod_discount": 9000,
                    "prod_thumbnail": "http://",
                    "brand_name": "미정",
                },
                request_only=True,
                response_only=False,  
            ),
        ],
    )
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
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_201_CREATED)

@extend_schema(
    tags=["상품"],
    summary="새로운 브랜드를 추가합니다.",
)
class BrandCreateAPIView(CreateAPIView):
    permission_classes = [IsUserOrReadonly]
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
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["상품"],
)
class HashtagModelViewSet(ModelViewSet):
    permission_classes = [IsUserOrReadonly]

    def get_serializer_class(self):
        if self.action == 'create':
            return HashtagCreateSerializer
        return HashtagSerializer

    @extend_schema(
        summary="새로운 해시태그를 조회합니다.",
        parameters=[
            OpenApiParameter(
                name="room_type",
                description="룸타입을 지정해 주세요.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        queryParams = request.query_params
        ret = {}
        if 'room_type' in queryParams:
            roomType = queryParams['room_type']
            hashSerializer = HashtagSerializer(
                Hashtag.objects.filter(
                    room_type__startswith=roomType,
                    is_active='Y'), 
                many=True)
            ret = hashSerializer.data
        return Response(ret, status=status.HTTP_200_OK)

    @extend_schema(
        summary="새로운 해시태그를 생성합니다.",
        examples=[
            OpenApiExample(
                "Valid example 1",
                summary="테스트 해시태그 생성 예시",
                description="인증이 확인된 사용자만 해시태그를 생성할 수 있습니다.",
                value={
                    "hash_name": "테스트",
                    "room_type": "RT90",
                    "hash_desc": "해시태그에 대한 설명",
                    "hash_thumbnail": "http://",
                    "hash_avg_price": 10000,
                },
                request_only=True,
                response_only=False,  
            ),
        ],
    )
    def create(self, request, *args, **kwargs):
        data = {}
        try:
            response = super().create(request, *args, **kwargs)
            # TODO: response를 출력하기 위한 LOGGER 추가
            data['message'] = "해시태그가 정상적으로 추가되었습니다."
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            data['message'] = str(e)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class HashtagAPIView(ListCreateAPIView):
    permission_classes = [IsUserOrReadonly]
    serializer_class = HashtagSerializer

    def get(self, request, id = None, *args, **kwargs):
        if(id is None ):
            return Response({"success": False}, status=status.HTTP_404_NOT_FOUND)
        hashSerializer = HashtagSerializer(Hashtag.objects.get(hash_seq=id))
        ret = hashSerializer.data
        return Response(ret, status=status.HTTP_200_OK)

@extend_schema(
    tags=["상품"],
    summary="상품과 해시태그를 연결합니다.",
)
class ProductHashtagCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductHashtagCreateSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        try:
            response = super().create(request, *args, **kwargs)
            # TODO: response를 출력하기 위한 LOGGER 추가
            data['message'] = "상품과 해시태그가 정상적으로 연결되었습니다."
            return Response(data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            data['message'] = "등록되지 않은 prod_name입니다."
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        except Hashtag.DoesNotExist:
            data['message'] = "등록되지 않은 hash_name입니다."
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            data['message'] = str(e)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["상품"],
    summary="해시태그를 위한 카테고리를 조회합니다.",
    parameters=[
        OpenApiParameter(
            name="room_type",
            description="룸타입을 지정해 주세요.",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        ),
    ],
)
class HashtagCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = HashtagSerializer

    def get(self, request):
        filt = "RT"
        if 'room_type' in request.query_params:
            filt = request.query_params['room_type']
        
        uniqueHashRoomTypeList = list(
            Hashtag.objects.filter(
                is_active="Y",
                room_type__startswith=filt
            ).values_list(
                'room_type', flat=True
            ).distinct())
        hashCateQs = HashtagCategory.objects.filter(room_type__in=uniqueHashRoomTypeList)

        # TODO: Serializer로 처리
        filteredDictList =[
            {
                'room_type': hashCateQ.room_type,
                'category': hashCateQ.category,
                'thumbnail': hashCateQ.thumbnail,
                'description': hashCateQ.description,
            }
            for hashCateQ in hashCateQs
        ]
        
        return Response(filteredDictList, status=status.HTTP_200_OK)

