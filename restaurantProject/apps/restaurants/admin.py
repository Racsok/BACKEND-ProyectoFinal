from django.contrib import admin
from .models import *

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "direction"]
    
class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "personCapacity"]
    
class TablesRestaurantAdmin(admin.ModelAdmin):
    list_display = ["table", "restaurant"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["waiter", "tableRestaurant"]

class BillAdmin(admin.ModelAdmin):
    list_display = ["order", "cost", "tipPorcent"]

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ["order", "product"]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(TablesRestaurant, TablesRestaurantAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)