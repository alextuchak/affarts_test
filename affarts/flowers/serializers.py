from rest_framework import serializers
from .models import Flower, Lot, Order
from users.serializers import UserForLotSerializers


class FlowerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ('id', 'name', 'color')
        read_only_fields = ('id',)


class LotCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ('id', 'seller', 'flower', 'quantity', 'price', 'visibility')
        read_only_fields = ('id',)


class LotSerializers(serializers.ModelSerializer):
    seller = UserForLotSerializers()
    flower = FlowerSerializers()

    class Meta:
        model = Lot
        fields = ('seller', 'flower', 'quantity', 'price',)
        read_only_fields = ('id',)


class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'buyer', 'lot', 'created_at')


class OrderShowSerializers(serializers.ModelSerializer):
    buyer = UserForLotSerializers()
    lot = LotSerializers()

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'lot', 'created_at')
