from rest_framework import serializers
<<<<<<< HEAD
from .models import section_and_caterogy, products, package


class SectionAndCategorySerializer(serializers.ModelSerializer):
=======
from .models import products, package, section_and_caterogy


class SectionAndCatogorySerializer(serializers.ModelSerializer):
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
    class Meta:
        model = section_and_caterogy
        fields = ['id', 'name']

<<<<<<< HEAD
class PackageSerializer(serializers.ModelSerializer):
=======
class PachageSerializer(serializers.ModelSerializer):
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
    class Meta:
        model = package
        fields = ['id', 'name', 'cost', 'quantity', 'image']

class ProductsSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    package = PackageSerializer(read_only=True, many=True)
=======
    category = SectionAndCatogorySerializer(read_only=True, many=True)
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
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