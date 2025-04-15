# Generated by Django 4.2.7 on 2025-04-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0018_staff_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='contract_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Стоимость контракта'),
        ),
        migrations.AddField(
            model_name='program',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон для связи'),
        ),
    ]
