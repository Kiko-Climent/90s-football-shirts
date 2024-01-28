from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_cart, name='shopping_cart'),
    path('add/<item_id>/', views.add_to_shopping_cart, name='add_to_shopping_cart'),
    path('update/<item_id>/', views.update_shopping_cart, name='update_shopping_cart'),
]
