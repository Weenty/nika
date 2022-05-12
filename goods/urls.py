from django.urls import path
from .views import *
urlpatterns = [
    path('sections/<int:pk>/', SectionsListId.as_view()),
    path('categorys/', CategorysList.as_view()),
    path('categorys/<int:category_id>/', CategorysList.as_view()),
    path('sections/', SectionsList.as_view()),
    path('products/', ProductsView.as_view()),
    path('products/<int:product_id>/', ProductsViewId.as_view()),
]
