from django.db import models
from django.contrib.auth.models import User


#modelos
from apps.restaurants.models import Bill

# Create your models here.
#Mesero
class Waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    CHARGE_CHOICES = [('MG', 'MANAGER'),('AT', 'ADMINTABLES'),('EX', 'EXTRA')]
    charge = models.CharField(max_length=2, choices=CHARGE_CHOICES, default='EX', unique=True)
    
    def __str__(self) -> str:
        return f"user: {self.user}, charge: {self.charge}"
    
class WaiterShift(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
class TipWaiter(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    waiter = models.OneToOneField(Waiter, on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False, blank=True, null=False)
