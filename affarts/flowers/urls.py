from django.urls import path
from .views import FlowerCreateView, LotView, OrderView, LotReviewView, SellerReviewView

app_name = 'flowers'

urlpatterns = [
    path('add/', FlowerCreateView.as_view(), name='flowers'),
    path('lot/', LotView.as_view(), name='lot'),
    path('order/create/', OrderView.as_view(), name='order_create'),
    path('order/get/', OrderView.as_view(), name='order_get'),
    path('review/lot/post/', LotReviewView.as_view(), name='lot_review_post'),
    path('review/lot/get/', LotReviewView.as_view(), name='lot_review_post'),
    path('review/seller/post/', SellerReviewView.as_view(), name='seller_review_post'),
    path('review/seller/get/', SellerReviewView.as_view(), name='seller_review_post'),

    ]
