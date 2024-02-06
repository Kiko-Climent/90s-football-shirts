from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:product_id>/', views.rating_product, name='rating_product'),
]
