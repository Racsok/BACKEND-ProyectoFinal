from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "cost_per_unit", "all_restaurants"]
    


admin.site.register(Products, ProductsAdmin)