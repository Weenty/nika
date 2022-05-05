from rest_framework import serializers
from .models import *


class SectionAndCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = section_and_caterogy
        fields = ['id', 'name']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = ['image']

class PackageSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    class Meta:
        model = package
        fields = ['id', 'name', 'cost', 'quantity', 'image']

class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    package = PackageSerializer(many=True, read_only=True)
    class Meta:
        model = products
        fields = [
        'id',
        'name',
        'discription',
        'discount',
        'purpose',
        'brand',
        'manufacturer',
        'best_before_date',
        'composition',
        'rating',
        'number_of_views',
        'package',
        'category'
        ]
