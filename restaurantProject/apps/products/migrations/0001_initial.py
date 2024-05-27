# Generated by Django 5.0.6 on 2024-05-27 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('cost_per_unit', models.IntegerField(default=0)),
                ('all_restaurants', models.BooleanField()),
            ],
        ),
    ]