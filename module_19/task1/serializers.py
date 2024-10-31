import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'description', 'cost')


class BuyerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    balance = serializers.DecimalField(max_digits=7, decimal_places=2)
    age = serializers.IntegerField()


class BuyerModel:
    def __init__(self, name, balance, age):
        self.name = name
        self.balance = balance
        self.age = age


def encode():
    model = BuyerModel('Nick', 1000, 18)
    model_sr = BuyerSerializer(model)
    json = JSONRenderer().render(model_sr.data)
    print(model_sr, type(model_sr))
    print(json, type(json))


def decode():
    sr = io.BytesIO(b'{"name":"Nick","balance":"1000.00","age":18}')
    data = JSONParser().parse(sr)
    serializer = BuyerSerializer(data=data)
    serializer.is_valid()
    data_sr = serializer.validated_data
    print(sr, type(sr))
    print(data_sr, type(data_sr))
