from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'type', 'username')
        read_only_fields = ('id',)
        extra_kwargs = {"password": {"write_only": True}}


class UserForLotSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('type', 'username')
        read_only_fields = ('id',)