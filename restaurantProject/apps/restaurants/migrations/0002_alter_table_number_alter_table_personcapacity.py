# Generated by Django 5.0.6 on 2024-06-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='personCapacity',
            field=models.IntegerField(default=1),
        ),
    ]