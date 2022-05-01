from goods.models import section_and_caterogy, products
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404

class SectionsList(APIView):
    def get_section(self):
        return get_list_or_404(section_and_caterogy.objects.filter(parent = None))
    
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
    
    def get_product_object(self, product_id):
        return get_object_or_404(products.objects.filter(id = product_id))

    def get(self, request, product_id=None):
        if product_id:
            serializer = serializers.ProductsSerializer(self.get_product_object(product_id)).data
        else:
            serializer = serializers.ProductsSerializer(self.get_products_list(), many=True).data
        return Response(serializer)