from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('past_orders/<order_number>', views.past_orders, name='past_orders'),
]
