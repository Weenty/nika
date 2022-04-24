import requests
from json import loads
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import status
from goods.models import package
from rest_framework import generics

def actiovation_post(request, uid, token):
    res = requests.post('http://127.0.0.1:8000/auth/users/activation/', data={"uid": uid, "token": token})
    if res.status_code == 204: return JsonResponse({"uid": "You have successfully verified your email"})
    else:
        return JsonResponse(loads(res.text))


class BacketView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BacketSerializer

    def get_backet(self, user_id):
        return get_list_or_404(basket.objects.filter(user_id=user_id))

    def get(self, request):
        user_id = request.user.id
        serializes = BacketSerializer(self.get_backet(user_id), many=True)
        return Response(serializes.data)

    def post(self, request):
        # product = ProductsSerializer(products.objects.get(id = request.data.get("products"))).data
        # packages = PackageSerializer(package.objects.get(id = request.data.get("package"))).data
        # data = request.data
        # data["user"] = request.user.id
        # data["products"] = product
        # data["package"] = packages
        # print(data)
        serializer = BacketSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BacketView(generics.ListCreateAPIView):
#     queryset = basket.objects.all()
#     serializer_class = BacketSerializer
#     permission_classes = [IsAuthenticated]