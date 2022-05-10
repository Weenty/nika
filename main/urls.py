from django.urls import path
from .views import *
urlpatterns = [
    path('basket/', BacketView.as_view()), 
    path('basket/<int:basket_id>/', BacketDeleteView.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:order_id>/', OrderListView.as_view()),
    path('comments/<int:product_id>/', CommentsView.as_view()),
    path('comments/<int:product_id>/<int:comment>/', CommentsDeleteUpdateView.as_view())
]
