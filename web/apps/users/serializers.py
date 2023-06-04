from rest_framework import serializers
from core.serializers import CreateSerializer

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]
        read_only_fields = fields

class UserCreateSerializer(CreateSerializer):
    representation_serializer_class = UserSerializer
    password2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
        )
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password2": "This is different with password."})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.createMember(**validated_data)
