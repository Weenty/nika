from django.urls import path
from .views import SectionsList, CategorysList, Products

urlpatterns = [
    path('sections/<int:pk>/', SectionsList.as_view()),
    path('sections/', SectionsList.as_view()),
    path('categorys/', CategorysList.as_view()),
    path('categorys/<int:pk>/', CategorysList.as_view()),
    path('products/<int:pk>/', Products.as_view()),
]
