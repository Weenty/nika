from django.urls import path
from .views import *
urlpatterns = [
    path('sections/<int:pk>/', SectionsList.as_view()),
    path('categorys/', CategorysList.as_view()),
    path('categorys/<int:pk>/', CategorysList.as_view()),
    path('sections/', SectionsList.as_view()),
    path('products/', Products.as_view()),
]
