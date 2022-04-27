from rest_framework import serializers
from .models import *

class BacketSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=products.objects.all())
    package = serializers.PrimaryKeyRelatedField(queryset=package.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=users.objects.all())
    class Meta:
        model = basket
        fields = [
            'products',
            'package',
            'quantity',
            'user'
        ]

class CommentsSerializer(serializers.ModelSerializer):
    user = models.ForeignKey('users', on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    class Meta:
        model = comments
        fields = [
            'user',
            'products', 
            'title',
            'text',
            'grade'
        ]