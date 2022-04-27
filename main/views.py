import requests
from json import loads
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_list_or_404

def actiovation_post(request, uid, token):
    res = requests.post('http://127.0.0.1:8000/auth/users/activation/', data={"uid": uid, "token": token})
    if res.status_code == 204: return JsonResponse({"uid": "You have successfully verified your email"})
    else:
        return JsonResponse(loads(res.text))


class BacketView(generics.ListCreateAPIView):
    queryset = basket.objects.all()
    serializer_class = BacketSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user_id = request.user.id
        serializes = BacketSerializer(basket.objects.filter(user_id = user_id), many=True)
        return Response(serializes.data)

    def create(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = BacketSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsView(generics.ListCreateAPIView):
    """
    Для get-запроса необходим только path-параметр, содержащий id интересующего продукта. 
    Для post-запроса структура подобного типа: 
        {
            "title": string, 
            "text": string,
            "grade": int
        }
    """ 
    queryset = comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_categorys_in_section(self, id):
        return get_list_or_404(comments.objects.filter(products = id))

    def list(self, request, product_id):

        id = product_id or request.query_params.get('product_id')
        serializer = CommentsSerializer(self.get_categorys_in_section(id), many=True)
        return Response(serializer.data)
    
    def create(self, request, product_id):
        id = product_id or request.query_params.get('product_id')
        data = request.data
        data['products'] = id
        data["user"] = request.user.id
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
