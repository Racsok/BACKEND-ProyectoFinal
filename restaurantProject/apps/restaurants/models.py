from django.db import models

#modelos
from apps.products.models import Products
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    direction = models.CharField(max_length=150, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name

class Table(models.Model):
    number = models.IntegerField(default=1,null=False, blank=False)
    personCapacity = models.IntegerField(default=1, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"Table {self.number}"
    
    
    
class TablesRestaurant(models.Model):
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f"mesa: {self.table} res: {self.restaurant}"
    
class Order(models.Model):
    waiter = models.ForeignKey('users.Waiter', on_delete=models.DO_NOTHING)
    tableRestaurant = models.ForeignKey(TablesRestaurant, on_delete=models.DO_NOTHING)  
    
    def __str__(self) -> str:
        return f"mesero: {self.waiter}, mesa: {self.tableRestaurant}"

class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    cost = models.IntegerField(default=100)#NO SE QUE TIPO ES
    tipPorcent = models.IntegerField(default=100)#NO SE QUE TIPO ES
    finalCost = models.IntegerField(default=100)#NO SE QUE TIPO ES

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
     