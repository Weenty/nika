from rest_framework import serializers
from goods.serializers import ProductsSerializer, PackageSerializer
from .models import *

class BacketSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(read_only=True)
    package = PackageSerializer(read_only=True)
    class Meta:
        model = basket
        fields = [
            'products',
            'package',
            'quantity',
        ]
