from rest_framework import serializers
from .models import products, package, section_and_caterogy


class SectionAndCatogorySerializer(serializers.ModelSerializer):
    class Meta:
        model = section_and_caterogy
        fields = ['id', 'name']

class PachageSerializer(serializers.ModelSerializer):
    class Meta:
        model = package
        fields = ['id', 'name', 'cost', 'quantity', 'image']

class ProductsSerializer(serializers.ModelSerializer):
    category = SectionAndCatogorySerializer(read_only=True, many=True)
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
        'package'
        ]