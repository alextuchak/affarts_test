from django.urls import path
from .views import FlowerCreateView, LotView

app_name = 'flowers'

urlpatterns = [
    path('add/', FlowerCreateView.as_view(), name='flowers'),
    path('lot/', LotView.as_view(), name='lot')
    ]
