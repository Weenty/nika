from xml.dom import ValidationErr
import requests
from json import loads
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404


def actiovation_post(request, uid, token):
    res = requests.post(
        'http://127.0.0.1:8000/auth/users/activation/', data={"uid": uid, "token": token})
    if res.status_code == 204:
        return JsonResponse({"uid": "You have successfully verified your email"})
    else:
        return JsonResponse(loads(res.text))

class BacketDeleteView(generics.DestroyAPIView):
    """
    Требуется токен аутефикации!
    """
    serializer_class = BacketSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, basket_id, user_id):
        result = get_object_or_404(basket.objects.filter(id = basket_id, user=user_id))
        if result.ordered == 1:
            raise IndexError('Заказанный товар не подлежит изменению или удалению')
        return result

    def delete(self, request, basket_id):
        basket_id = basket_id or request.query_params.get('basket_id')
        try:
            result = self.get_object(basket_id, request.user.id)
            result.delete()
            return Response({"detail":f'Товар {result.products.name} был удален из корзины'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, basket_id):
        """
        Требуется токен аутефикации!
        {
            "products": integer, 
            "package": integer,
            "quantity": integer
        }
        """
        try:
            data = request.data
            data["user"] = request.user.id
            result = self.get_object(basket_id, request.user.id)
            serializer = BacketSerializer(result, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BacketView(APIView):
    """
    Требуется токен аутефикации!
    """
    queryset = basket.objects.all()
    serializer_class = BacketSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        serializes = BacketSerializer(
            basket.objects.filter(user_id=user_id), many=True)
        return Response(serializes.data)

    def post(self, request):
        """
        Требуется токен аутефикации!
        {
            "products": integer, 
            "package": integer,
            "quantity": integer
        }
        Если не указывать quantity в теле запроса, то стандартом выставится 1 для параметра quantity
        """
        data = request.data
        data["user"] = request.user.id
        serializer = BacketSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            basket_exists = basket.objects.filter(package=data['package'], user=data["user"]).exists()
            if basket_exists:
                raise ValueError("Данный товар уже был добавлен в корзину")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get_order_list(self, order_id):
        return get_list_or_404(orders_list.objects.filter(order=order_id))

    def get(self, request, order_id=None):
        """
        Требуется токен аутефикации!
        """
        order_id = order_id or request.query_params.get('order_id')
        try:
            order.objects.get(id=order_id, user=request.user.id)
            serializer = OrderListSerializer(
                self.get_order_list(order_id), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "Страница не найдена"}, status=status.HTTP_404_NOT_FOUND)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get_orders(self, user_id):
        return get_list_or_404(order.objects.filter(user=user_id))

    def get(self, request):
        """
        Требует токен аутефикации!
        """
        serializer = OrderSerializerForGet(
            self.get_orders(request.user.id), many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Запрос в таком формате: В order_list указывать id пакета. На данный момент можно добавлять лишь один товар в заказ, 
        но это не на долго!
            {
        "point_of_issue": 1,
        "receiving_method": 1,
        "payment_method": 1,
        "comment": "текст",
        "order_list": [сюда передаем закидываем массив id корзины]
            }
        Требуется токен аутефикации!
        """
        data = request.data
        user = request.user.id
        data["user"] = user
        serializer = OrderSerializerForPost(data=data)
        if serializer.is_valid(raise_exception=True):
            # КОД СЫРОЙ, НЕОБХОДИМО ПЕРЕРАБОТАТЬ
            try:
                order = serializer.save()
                quantity_list = []
                for basket_id in data["order_list"]:
                    basket_object = basket.objects.get(id=basket_id, user=user)
                    if basket_object.ordered == 1:
                        raise IndexError('Один или несколько товаров корзины уже заказаны!')
                    data = {
                        "product": basket_object.products.id,
                        "package": basket_object.package.id,
                        "quantity": basket_object.quantity,
                        "cost": basket_object.package.cost,
                        "order": order.id
                    }
                    serializer = OrderListSerializer(data=data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()

                    if getattr(package.objects.get(id=basket_object.package.id), 'quantity')-basket_object.quantity >= 0:
                        quantity_list.append((basket_object.package.id,basket_object.quantity))
                    else: raise ValueError(f'Невозможно заказть {basket_object.quantity} из пакета {basket_object.package.name}, так как количетство товара - {getattr(package.objects.get(id=basket_object.package.id), "quantity")}')
                
                for qu in quantity_list:
                    package_id, quantity = qu
                    ordered = basket.objects.get(package=package_id, user=user)
                    ordered.ordered = 1
                    ordered.save()

                    new_package = package.objects.get(id=package_id)
                    new_package.quantity = (new_package.quantity - quantity)
                    new_package.save()

                return Response({"detail": "Ваш заказ успешно принят!", "id": order.id}, status=status.HTTP_201_CREATED)
            except Exception as e:
                if order:
                    order.delete()
                    orders_list.objects.filter(order=order).delete()
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsDeleteUpdateView(APIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_comment(self, comment, id, user):
        return get_object_or_404(comments.objects.filter(id=comment, products=id, user=user))

    def delete(self, request, product_id, comment):
        product_id = product_id or request.query_params.get('basket_id')
        try:
            result = self.get_comment(comment, product_id, request.user.id)
            result.delete()
            return Response({"detail":'Комментарий был удален'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id, comment):
        try:
            data = request.data
            data["user"] = request.user.id
            data["products"] = product_id
            result = self.get_comment(comment, product_id, request.user.id)
            serializer = CommentsSerializer(result, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CommentsView(APIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_comments(self, id):
        return get_list_or_404(comments.objects.filter(products=id))

    def get(self, request, product_id):
        """
        Для get-запроса необходим только path-параметр, содержащий id интересующего продукта. 
        """
        id = product_id or request.query_params.get('product_id')
        serializer = CommentsSerializer(
            self.get_comments(id), many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        """
            Для post-запроса структура подобного типа. (title и text можно оставить пустыми)
            {
                "title": string, 
                "text": string,
                "grade": int
            }
        """
        id = product_id or request.query_params.get('product_id')
        if not basket.objects.filter(user=request.user.id, ordered=1, products=id).exists():
            return Response({"datail": 'Вы не заказали данный товар, поэтому не можете оставлять отзывы'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        data['products'] = id
        data['user'] = request.user.id
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
