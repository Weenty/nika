from rest_framework import serializers
from main.models import *

class BacketSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=products.objects.all())
    package = serializers.PrimaryKeyRelatedField(
        queryset=package.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    ordered = serializers.IntegerField(read_only=True)
    class Meta:
        model = basket
        fields = [
            'id',
            'products',
            'package',
            'quantity',
            'user',
            'ordered'
        ]


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    products = serializers.PrimaryKeyRelatedField(queryset = products.objects.all())
    class Meta:
        model = comments
        fields = [
            'user',
            'products',
            'title',
            'text',
            'grade'
        ]



class OrderListSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=products.objects.all())
    package = serializers.PrimaryKeyRelatedField(queryset=package.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=order.objects.all())
    cost = serializers.DecimalField(read_only=True, max_digits=7, decimal_places=0)
    class Meta:
        model = orders_list
        fields = [
            'cost',
            'quantity',
            'order',
            'product',
            'package',
        ]


class OrderSerializerForGet(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    payment_method = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    receiving_method = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    point_of_issue = serializers.SlugRelatedField(
        read_only=True,
        slug_field='sity'
    )
    final_cost = serializers.DecimalField(read_only=True, max_digits=7, decimal_places=0)
    
    class Meta:
        model = order
        fields = [
            'id',
            'user',
            'final_cost',
            'comment',
            'payment_method',
            'receiving_method',
            'point_of_issue'
        ]


class OrderSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = [
            'user',
            'comment',
            'payment_method',
            'receiving_method',
            'point_of_issue'
        ]