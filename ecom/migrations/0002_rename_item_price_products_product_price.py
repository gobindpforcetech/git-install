# Generated by Django 4.1.5 on 2023-01-26 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='item_price',
            new_name='product_price',
        ),
    ]
