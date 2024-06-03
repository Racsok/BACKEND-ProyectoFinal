from django.db import models
from django.contrib.auth.models import User




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
    
