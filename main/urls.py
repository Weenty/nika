from django.urls import path
from .views import *
urlpatterns = [
    path('basket/', BacketView.as_view()), 
    path('orders/', OrderView.as_view()),
    path('orders/<int:order_id>', OrderView.as_view())
]
