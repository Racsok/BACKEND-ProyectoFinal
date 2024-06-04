from django.db import models

#modelos
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
        return f"{self.number}"
    
    
    
class TablesRestaurant(models.Model):
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f"{self.table} {self.restaurant}"
    
class Order(models.Model):
    waiter = models.ForeignKey('users.Waiter', on_delete=models.DO_NOTHING)
    tableRestaurant = models.ForeignKey(TablesRestaurant, on_delete=models.DO_NOTHING)  
    
    def __str__(self) -> str:
        return f"{self.waiter} {self.tableRestaurant}"

class Bill(models.Model):
    order = models.ForeignKey(Order, blank=True, on_delete=models.DO_NOTHING)
    cost = models.FloatField(default=100)
    tipPorcent = models.FloatField()
    finalCost = models.FloatField(default=None, blank=True, null=True)
    

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey('products.Products', on_delete=models.DO_NOTHING)
     