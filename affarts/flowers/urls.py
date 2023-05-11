from django.urls import path
from .views import FlowerCreateView, LotView, OrderView

app_name = 'flowers'

urlpatterns = [
    path('add/', FlowerCreateView.as_view(), name='flowers'),
    path('lot/', LotView.as_view(), name='lot'),
    path('order/create/', OrderView.as_view(), name='order_create'),
    path('order/get/', OrderView.as_view(), name='order_get')
    ]
