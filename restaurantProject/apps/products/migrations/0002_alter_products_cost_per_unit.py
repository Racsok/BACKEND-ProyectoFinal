# Generated by Django 5.0.6 on 2024-06-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cost_per_unit',
            field=models.FloatField(default=1),
        ),
    ]
