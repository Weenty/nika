<<<<<<< HEAD
from goods.models import section_and_caterogy, products, package
=======
from goods.models import products, package, section_and_caterogy
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404

class SectionsList(APIView):
<<<<<<< HEAD
    def get_section(self):
        return get_list_or_404(section_and_caterogy.objects.filter(parent = None))
=======
    def get_section_categorys(self, id):
        return get_list_or_404(section_and_caterogy.objects.filter(section=id, parent=None))
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
    
    def get_categorys_in_section(self, id):
        return get_list_or_404(section_and_caterogy.objects.filter(parent = id))
    
    def get(self, request, pk=None):
   
        id = pk or request.query_params.get('id')
        if id:
            serializer = serializers.SectionAndCategorySerializer(self.get_categorys_in_section(id), many=True)
        else:
            serializer = serializers.SectionAndCategorySerializer(self.get_section(), many=True)

        return Response(serializer.data)

class CategorysList(APIView):
    def get_products_in_category(self, id):
        return get_list_or_404(products.objects.filter(category=id))
    
    def get_category_list(self):
        return get_list_or_404(section_and_caterogy.objects.filter(parent__isnull = False))

    def get(self, request, pk=None):
   
        id = pk or request.query_params.get('id')
        if id:
            serializer = serializers.ProductsSerializer(self.get_products_in_category(id), many=True)
        else:
            serializer = serializers.SectionAndCategorySerializer(self.get_category_list(), many=True)

        return Response(serializer.data)

class Products(APIView):
    def get_products_list(self):
        return get_list_or_404(products.objects.all())

    def get(self, request, pk=None):
<<<<<<< HEAD
        return Response(serializers.ProductsSerializer(self.get_products_list(), many=True).data)
=======
        id = pk or request.query_params.get('id')
        if id:
            serialize_product = serializers.ProductsSerializer(self.get_product_object(id))
            serialize_package = serializers.PachageSerializer(self.get_package(serialize_product.data['package']))
            serialize_product.data['package'] = serialize_package
        else: serialize_product = serializers.ProductsSerializer(self.get_products_list(), many=True)
        return Response(serialize_product.data)
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
