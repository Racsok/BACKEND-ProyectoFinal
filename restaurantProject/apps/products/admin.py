from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "cost_per_unit", "all_restaurants"]
    
class ProductsRestauranAdmin(admin.ModelAdmin):
    list_display = ["product", "restaurant"]


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsRestaurant, ProductsRestauranAdmin)