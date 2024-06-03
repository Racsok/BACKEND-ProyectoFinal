# Generated by Django 5.0.6 on 2024-06-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_bill_cost_alter_bill_finalcost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='cost',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='bill',
            name='finalCost',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='tipPorcent',
            field=models.FloatField(),
        ),
    ]
