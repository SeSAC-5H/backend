from rest_framework import serializers
from core.serializers import CreateSerializer
from stores.models import Stores, Report


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


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude = ["updated_at", "created_at"]


class ReportCreateSerializer(CreateSerializer):
    representation_serializer_class = StoreSerializer

    class Meta:
        model = Report
        fields = [
            "report_name",
            "report_address",
            "report_tel",
        ]

    def create(self, validated_data):
        return Report.objects.create(**validated_data)
