from django.urls import path
from .views import *
urlpatterns = [
    path('sections/<int:pk>/', SectionsList.as_view()),
    path('categorys/', CategorysList.as_view()),
    path('categorys/<int:pk>/', CategorysList.as_view()),
<<<<<<< HEAD
    path('sections/', SectionsList.as_view()),
=======
    path('products/<int:pk>/', Products.as_view()),
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
    path('products/', Products.as_view()),
]
