from goods.models import section_and_caterogy, products
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import filters

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
    def get_products_in_category(self, category_id):
        print('products.objects.filter(category=category_id)')
        return get_list_or_404(products.objects.filter(category=category_id))
    
    def get_category_list(self):
        return get_list_or_404(section_and_caterogy.objects.filter(parent__isnull = False))

    def get(self, request, category_id=None):
        category_id = category_id or request.query_params.get('category_id')
        if category_id:
            serializer = serializers.ProductsSerializer(self.get_products_in_category(category_id), many=True)
        else:
            serializer = serializers.SectionAndCategorySerializer(self.get_category_list(), many=True)

        return Response(serializer.data)

class ProductsViewId(APIView):

    def get_product_object(self, product_id):
        return get_object_or_404(products.objects.filter(id = product_id))

    def get(self, request, product_id):
        serializer = serializers.ProductsSerializer(self.get_product_object(product_id))
        return Response(serializer.data)

class ProductsView(generics.ListAPIView):
    
    queryset = products.objects.all()
    serializer_class = serializers.ProductsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']