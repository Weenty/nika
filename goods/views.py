from struct import pack
from goods.models import section, caterogy, products, package
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404

class SectionsList(APIView):
    def get_section_categorys(self, id):
        return get_list_or_404(caterogy.objects.filter(section=id))
    
    def get_sections_list(self):
        return get_list_or_404(section.objects.all())
    
    def get(self, request, pk=None):
   
        id = pk or request.query_params.get('id')
        if id:
            serializer = serializers.CategorySerializer(self.get_section_categorys(id), many=True)
        else:
            serializer = serializers.SectionSerializer(self.get_sections_list(), many=True)

        return Response(serializer.data)

class CategorysList(APIView):
    def get_category_products(self, id):
        return get_list_or_404(products.objects.filter(category=id))
    
    def get_category_list(self):
        return get_list_or_404(caterogy.objects.all())

    def get(self, request, pk=None):
   
        id = pk or request.query_params.get('id')
        if id:
            serializer = serializers.ProductsSerializer(self.get_category_products(id), many=True)
        else:
            serializer = serializers.CategorySerializer(self.get_category_list(), many=True)

        return Response(serializer.data)

class Products(APIView):
    def get_products_list(self):
        return get_list_or_404(products.objects.all())
    
    def get_product_object(self, id):
        return get_object_or_404(products.objects.filter(id))
    
    def get_package(pack):
        return package.objects.filter(id=pack)

    def get(self, request, pk=None):
        id = pk or request.query_params.get('id')
        if id:
            serialize_product = serializers.ProductsSerializer(self.get_product_object(id))
            serialize_package = serializers.PachageSerializer(self.get_package(serialize_product.data['package']))
            serialize_product.data['package'] = serialize_package
        return Response(serialize_product)