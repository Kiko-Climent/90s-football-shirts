from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_cart, name='shopping_cart'),
]
