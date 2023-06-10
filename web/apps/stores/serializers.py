from rest_framework import serializers
from core.serializers import CreateSerializer
from stores.models import Stores


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        exclude = ["updated_at", "created_at"]


class StoreCreateSerializer(CreateSerializer):
    representation_serializer_class = StoreSerializer

    class Meta:
        model = Stores
        fields = [
            "store_name",
            "store_id",
            "store_subcate",
            "store_time",
            "store_address_old",
            "store_address_new",
            "store_tel",
            "store_link",
            "store_coord_x",
            "store_coord_y",
            "store_insta",
            "store_item",
        ]

    def create(self, validated_data):
        return Stores.objects.create(**validated_data)
