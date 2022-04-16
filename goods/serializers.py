from pyexpat import model
from pyrsistent import field
from rest_framework import serializers
from .models import section, caterogy, products, package, image


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = caterogy
        fields = ['id', 'name']

class PachageSerializer(serializers.ModelSerializer):
    class Meta:
        model = package
        fields = ['id', 'name', 'cost', 'quantity', 'image']

class ProductsSerializer(serializers.ModelSerializer):
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
        'category',
        'package'
        ]