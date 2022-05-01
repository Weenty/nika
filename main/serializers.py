from rest_framework import serializers
from goods.serializers import ProductsSerializer
from main.models import *

class BacketSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=products.objects.all())
    package = serializers.PrimaryKeyRelatedField(
        queryset=package.objects.all())
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
    class Meta:
        model = orders_list
        fields = [
            'cost',
            'quantity',
            'order',
            'product',
            'package',
        ]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=users.objects.all())
    order_list = ProductsSerializer(many=True)
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
            'order_list',
            'comment',
            'payment_method',
            'receiving_method',
            'point_of_issue'
        ]