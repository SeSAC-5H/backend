from rest_framework import serializers
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
        try:
            brandObj = get_object_or_404(Brand, brand_name=data['brand_name'])
            data['brand_seq'] = brandObj
        except Brand.DoesNotExist:
            raise Http404("brand_name is not found in brands table.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('brand_name')
        return Product.objects.create(**validated_data)
