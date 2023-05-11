from rest_framework import serializers
from .models import Flower, Lot


class FlowerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ('id', 'name', 'color')
        read_only_fields = ('id',)


class LotCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ('id', 'seller', 'flower', 'quantity', 'price', 'visibility')