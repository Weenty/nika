from django.urls import path
from .views import *
urlpatterns = [
    path('backet/', BacketView.as_view())
]
