from rest_framework import serializers
from .models import section_and_caterogy, products, package


class SectionAndCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = section_and_caterogy
        fields = ['id', 'name']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = package
        fields = ['id', 'name', 'cost', 'quantity', 'image']

class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    package = PackageSerializer(read_only=True, many=True)
    class Meta:
        model = products
        fields = [
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
