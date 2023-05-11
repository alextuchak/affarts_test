# Generated by Django 4.2.1 on 2023-05-11 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flowers', '0008_alter_lot_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
    ]
