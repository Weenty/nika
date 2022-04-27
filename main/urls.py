from django.urls import path
from .views import *
urlpatterns = [
    path('basket/', BacketView.as_view())
]
