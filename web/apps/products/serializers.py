from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.serializers import CreateSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404

from products.models import Product, Brand, Hashtag, ProductHashtag

class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='get_brand_name')

    class Meta:
        model = Product
        fields = [
            'prod_name',
            'prod_link',
            'prod_price',
            'prod_discount',
            'prod_thumbnail',
            'brand_name'
        ]
        

class ProductCreateSerializer(CreateSerializer):
    representation_serializer_class = ProductSerializer
    brand_name = serializers.CharField(required=True)

    class Meta:
        model = Product
        fields = [
            'prod_name',
            'prod_link',
            'prod_price',
            'prod_discount',
            'prod_thumbnail',
            'brand_name',
        ]
    
    def validate(self, data):
        brandObj = get_object_or_404(Brand, brand_name=data['brand_name'])
        data['brand_seq'] = brandObj
        return data
    
    def create(self, validated_data):
        validated_data.pop('brand_name')
        return Product.objects.create(**validated_data)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = [
            'updated_at',
            'created_at'
        ]

class BrandCreateSerializer(CreateSerializer):
    representation_serializer_class = BrandSerializer
    brand_name = serializers.CharField(
        validators=[
            UniqueValidator(queryset=Brand.objects.all())
        ]
    )

    class Meta:
        model = Brand
        fields = [
            'brand_name',
            'brand_link',
        ]
    
    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = [
            'hash_seq',
            'hash_name',
            'room_type',
            'hash_desc',
            'hash_thumbnail',
        ]

class HashtagCreateSerializer(CreateSerializer):
    representation_serializer_class = HashtagSerializer

    class Meta:
        model = Hashtag
        fields = [
            'hash_name',
            'room_type',
        ]
    
    def create(self, validated_data):
        return Hashtag.objects.create(**validated_data)

class ProductHashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHashtag
        exclude = [
            'updated_at',
            'created_at'
        ]

class ProductHashtagCreateSerializer(CreateSerializer):
    representation_serializer_class = ProductHashtagSerializer
    prod_name = serializers.CharField(max_length=100)
    hash_name = serializers.CharField(max_length=100)

    class Meta:
        model = ProductHashtag
        fields = [
            'prod_name',
            'hash_name',
        ]
    
    def create(self, validated_data):
        prodName = validated_data.pop('prod_name')
        hashName = validated_data.pop('hash_name')
        validated_data['prod_seq'] = Product.objects.get(prod_name=prodName)
        validated_data['hash_seq'] = Hashtag.objects.get(hash_name=hashName)
        # raise Exception('hihi')
        return ProductHashtag.objects.create(**validated_data)