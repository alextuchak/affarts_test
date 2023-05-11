from django.db import models
from users.models import User

COLOR_CHOICES = (
    ('Red', 'Красный'),
    ('White', ',Белый'),
    ('Yellow', 'Желтый'),
    ('Purple', 'Фиолетовый'),
    ('Blue', 'Голубой')
)

RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Flower(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=16, choices=COLOR_CHOICES)


class Lot(models.Model):
    seller = models.ForeignKey(to=User, on_delete=models.CASCADE)
    flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    visibility = models.BooleanField(default=True)


class Order(models.Model):
    buyer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    lot = models.ForeignKey(to=Lot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class LotReview(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    lot = models.ForeignKey(to=Lot, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)


class SellerReview(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    seller = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='seller')
    text = models.CharField(max_length=512)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
