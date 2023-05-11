from django.db import models

COLOR_CHOICES = (
    ('Red', 'Красный'),
    ('White', ',Белый'),
    ('Yellow', 'Желтый'),
    ('Purple', 'Фиолетовый'),
    ('Blue', 'Голубой')
)


class Flower(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=16, choices=COLOR_CHOICES)


class Lot(models.Model):
    flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    visibility = models.BooleanField(default=True)

