from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.purchase_view, name='purchase'),
    path('purchase_success/<order_number>',
         views.purchase_success, name='purchase_success'),
    path('cache_purchase_data/', views.cache_purchase_data,
         name='cache_purchase_data'),
    path('wh/', webhook, name='webhook'),
]
