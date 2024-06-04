# Generated by Django 5.0.6 on 2024-06-04 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_cost_per_unit'),
        ('restaurants', '0004_alter_bill_cost_alter_bill_finalcost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsRestaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.products')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant')),
            ],
        ),
    ]
