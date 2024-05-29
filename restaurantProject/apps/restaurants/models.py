from django.db import models

#modelos
from ..products.models import Products 
from ..users.models import *
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    direction = models.CharField(max_length=150, blank=False, null=False)

class Table(models.Model):
    number = models.IntegerField()
    personCapacity = models.IntegerField()
    
    def __str__(self) -> str:
        return self.id
    
class TablesRestaurant(models.Model):
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.id
    
class Order(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    tableRestaurant = models.ForeignKey(TablesRestaurant, on_delete=models.DO_NOTHING)  

class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    cost = models.IntegerField(default=100)#NO SE QUE TIPO ES
    tipPorcent = models.CharField()#NO SE QUE TIPO ES
    finalCost = models.IntegerField()#NO SE QUE TIPO ES

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
     