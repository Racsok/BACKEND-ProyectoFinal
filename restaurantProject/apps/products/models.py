from django.db import models

# Create your models here.
from apps.restaurants.models import Restaurant
class Products(models.Model):
    name = models.CharField(max_length=60, null = False, blank = False)
    cost_per_unit = models.FloatField(default = 1, null = False, blank = False)
    all_restaurants = models.BooleanField()
    
    def __str__(self) -> str:
        return self.name
    
class ProductsRestaurant(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)