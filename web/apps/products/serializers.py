from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.serializers import CreateSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404

from products.models import Product, Brand

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = [
            'updated_at',
            'created_at'
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
